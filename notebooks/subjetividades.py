import plotly.express as px

def create_output_directories(base_path):
        """
        Creates necessary output directories for data img and notebooks.
        """
        
        folders_to_create = ['data','img','notebooks']
        
        list_of_folders = []
        
        for main_folder in folders_to_create:
                folder_path = base_path.joinpath(main_folder)
                folder_path.mkdir(parents=True, exist_ok=True)
                list_of_folders.append(folder_path)
        return list_of_folders

def create_data_directories(base_path):
        """
        Creates necessary output directories for data img and notebooks.
        """

        folders_to_create = ['raw','processed']

        list_of_folders = []

        for main_folder in folders_to_create:
                folder_path = base_path.joinpath(main_folder)
                folder_path.mkdir(parents=True, exist_ok=True)
                list_of_folders.append(folder_path)

        return list_of_folders#Pendiente

def create_bar_chart(df, column_name, file_name, plot_title,output_folder,visualize):
    unique_values = df[column_name].value_counts()

    # Create a bar chart using Plotly Express
    fig = px.bar(x=unique_values.index, y=unique_values.values)

    # Update layout if needed
    fig.update_layout(
        title='Bar Chart of '+ plot_title,
        xaxis_title="Unique Values",
        yaxis_title="Count"
    )
    fig.update_traces(texttemplate='%{y}',
                    textposition='outside')
    fig.update_xaxes(categoryorder='total descending')

    if visualize:
        # Show the plot
        fig.show()

    # Save the plot as an HTML file
    fig.write_html(output_folder.joinpath('bar_chart_'+file_name + '.html'))

def create_pie_chart(df, column_name, file_name, plot_title, output_folder, visualize):
    # Obtener los valores únicos y sus recuentos
    unique_values = df[column_name].value_counts()
    
    # # Convertir los recuentos a porcentajes
    total_count = unique_values.sum()
    unique_values = (unique_values / total_count) * 100
    
    # Crear el gráfico de pie usando Plotly Express
    fig = px.pie(
        values=unique_values.values,
        names=unique_values.index,
        title=f'Pie Chart of {plot_title}',
        labels={'names': '', 'values': ''},
        hole=0.3
    )
    
    # Agregar etiquetas de porcentaje y ajustar la posición de las etiquetas
    fig.update_traces(
        textinfo='percent+label',
        textfont_size=12,
        texttemplate='%{value:.2f}%',
        pull=[0.05] * len(unique_values.index),
        marker=dict(line=dict(color='#000000', width=1))
    )
    
    # Mostrar el gráfico si se especifica
    if visualize:
        fig.show()
    
    # Guardar el gráfico como archivo HTML
    fig.write_html(output_folder.joinpath('pie_chart_' + file_name + '.html'))
