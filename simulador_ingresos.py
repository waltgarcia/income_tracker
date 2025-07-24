import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="💰 Simulador de Ingresos", layout="wide")

# Título
st.title("💰 Simulador de Ingresos Mensuales")

# Sidebar con controles
with st.sidebar:
    st.header("Configuración")
    
    # Selector de mes y año
    mes = st.selectbox("Mes:", list(calendar.month_name[1:]), index=datetime.now().month-1)
    anio = st.number_input("Año:", min_value=2000, max_value=2100, value=datetime.now().year)
    
    # Ingresos
    ingreso_semana = st.number_input("Ingreso diario entre semana ($):", min_value=0, value=1000)
    ingreso_fin = st.number_input("Ingreso diario fin de semana ($):", min_value=0, value=1500)
    
    # Días no laborables
    dias_no_laborables = st.number_input("Número de días entre semana no laborables:", 
                                       min_value=0, max_value=23, value=0)
    
    st.button("Simular Ingresos", type="primary")

# Función para formatear dinero
def formato_dinero(x):
    return f"${x:,.2f}"

# Función principal de simulación
def simular_ingresos(mes, anio, ingreso_semana, ingreso_fin, dias_no_laborables):
    mes_num = list(calendar.month_name).index(mes)
    num_dias = calendar.monthrange(anio, mes_num)[1]
    
    # Crear dataframe con las fechas
    df = pd.DataFrame({
        'Fecha': pd.date_range(start=f'{anio}-{mes_num}-01', periods=num_dias),
        'Dia': range(1, num_dias+1)
    })
    
    # Determinar tipo de día
    df['DiaSemana'] = df['Fecha'].dt.day_name()
    df['EsFinDeSemana'] = df['Fecha'].dt.dayofweek >= 5  # 5=sábado, 6=domingo
    
    # Seleccionar días no laborables (solo entre semana)
    dias_semana = df[~df['EsFinDeSemana']].index
    if dias_no_laborables > 0 and len(dias_semana) > 0:
        no_laborables = np.random.choice(dias_semana, 
                                       size=min(dias_no_laborables, len(dias_semana)), 
                                       replace=False)
        df['EsNoLaborable'] = df.index.isin(no_laborables)
    else:
        df['EsNoLaborable'] = False
    
    # Calcular ingresos
    df['Ingresos'] = np.where(df['EsNoLaborable'], 0,
                             np.where(df['EsFinDeSemana'], ingreso_fin, ingreso_semana))
    
    # Sumatoria acumulada
    df['Ingresos_Acumulados'] = df['Ingresos'].cumsum()
    
    # Tipo de día para visualización
    df['TipoDia'] = np.where(df['EsNoLaborable'], 'No laborable',
                            np.where(df['EsFinDeSemana'], 'Fin de semana', 'Entre semana'))
    
    return df

# Ejecutar simulación
df = simular_ingresos(mes, anio, ingreso_semana, ingreso_fin, dias_no_laborables)

# Mostrar resultados en pestañas
tab1, tab2, tab3 = st.tabs(["Ingresos Diarios", "Sumatoria Acumulada", "Comparación ±$100"])

with tab1:
    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 5))
    
    colors = {'Entre semana': 'steelblue', 'Fin de semana': 'orange', 'No laborable': 'gray'}
    
    for tipo, color in colors.items():
        subset = df[df['TipoDia'] == tipo]
        ax.bar(subset['Dia'], subset['Ingresos'], color=color, label=tipo)
    
    ax.set_title(f"Ingresos diarios - {mes} {anio}")
    ax.set_xlabel("Día del mes")
    ax.set_ylabel("Ingresos ($)")
    ax.set_xticks(range(1, df['Dia'].max()+1))
    ax.yaxis.set_major_formatter('${x:,.0f}')
    ax.legend()
    st.pyplot(fig)

with tab2:
    # Gráfico de línea acumulada
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(df['Dia'], df['Ingresos_Acumulados'], 
            color='darkgreen', linewidth=2, marker='o', markersize=5)
    
    # Etiquetas de puntos
    for i, row in df.iterrows():
        if i % 3 == 0 or i == len(df)-1:  # Mostrar cada 3 días y el último
            ax.text(row['Dia'], row['Ingresos_Acumulados'], 
                   formato_dinero(row['Ingresos_Acumulados']), 
                   ha='center', va='bottom')
    
    ax.set_title(f"Sumatoria acumulada - {mes} {anio}")
    ax.set_xlabel("Día del mes")
    ax.set_ylabel("Ingresos acumulados ($)")
    ax.set_xticks(range(1, df['Dia'].max()+1))
    ax.yaxis.set_major_formatter('${x:,.0f}')
    st.pyplot(fig)

with tab3:
    # Comparación ±$100
    df['Ingresos_mas_100'] = np.where(df['EsNoLaborable'], 0,
                                     np.where(df['EsFinDeSemana'], 
                                             ingreso_fin + 100, 
                                             ingreso_semana + 100))
    
    df['Ingresos_menos_100'] = np.where(df['EsNoLaborable'], 0,
                                       np.where(df['EsFinDeSemana'], 
                                               max(0, ingreso_fin - 100), 
                                               max(0, ingreso_semana - 100)))
    
    df['Acum_mas_100'] = df['Ingresos_mas_100'].cumsum()
    df['Acum_menos_100'] = df['Ingresos_menos_100'].cumsum()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(df['Dia'], df['Ingresos_Acumulados'], 
            color='darkgreen', linewidth=2, label='Original')
    ax.plot(df['Dia'], df['Acum_mas_100'], 
            color='blue', linewidth=2, linestyle='--', label='+$100')
    ax.plot(df['Dia'], df['Acum_menos_100'], 
            color='red', linewidth=2, linestyle=':', label='-$100')
    
    ax.set_title("Comparación de sumatorias acumuladas")
    ax.set_xlabel("Día del mes")
    ax.set_ylabel("Ingresos acumulados ($)")
    ax.set_xticks(range(1, df['Dia'].max()+1))
    ax.yaxis.set_major_formatter('${x:,.0f}')
    ax.legend()
    st.pyplot(fig)

# Resumen de ingresos
st.subheader("📊 Resumen de ingresos:")

dias_laborables = len(df[df['Ingresos'] > 0])
total_ingresos = df['Ingresos'].sum()
promedio_laborable = total_ingresos / dias_laborables if dias_laborables > 0 else 0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Mes", f"{mes} {anio}")
    st.metric("Total ingresos", formato_dinero(total_ingresos))
    
with col2:
    st.metric("Días laborables", dias_laborables)
    st.metric("Días no laborables", len(df[df['Ingresos'] == 0]))
    
with col3:
    st.metric("Promedio diario (laborables)", formato_dinero(promedio_laborable))
    st.metric("Rango diario", f"{formato_dinero(df['Ingresos'].min())} - {formato_dinero(df['Ingresos'].max())}")