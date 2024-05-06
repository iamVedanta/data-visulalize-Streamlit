import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#set up page configuration

st.set_page_config(page_title="Data Visulizer", page_icon="📊", layout="centered")\


#set up title
st.title("📊 Data Visualizer Web App")


#getting the working directory of main.py file
working_dir = os.path.dirname(os.path.abspath(__file__)) #We do this because if someone runs the app from a different directory, the app should run without any issues.So we are not hardcoding the path.

#getting the path for data folder
folder_path = f'{working_dir}/data'

#list all the files in the data folder
files = [file for file in os.listdir(folder_path) if file.endswith('.csv')] #We are only interested in csv files

#dropdown to select the file
selected_file = st.selectbox("Select a file", files,index = None)


st.write(f"selected file: {selected_file}")

if selected_file:
    #get the complete path of the selected file
    file_path = f'{folder_path}/{selected_file}' #We are using f-string to concatenate the folder path and the selected file name
    #We can use file_path = os.path.join(folder_path,selected_file)


    #reading the csv file as a pandas dataframe
    df = pd.read_csv(file_path)

    col1, col2 = st.columns(2)
    # st.write (df.head())

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        #user selcetion of df columns 
        x_axis = st.selectbox("Select x-axis", options = columns + ['None'], index = None)
        y_axis = st.selectbox("Select y-axis", options = columns + ['None'], index = None)

        plot_list = ['Line Plot', 'Bar Plot', 'Scatter Plot', 'Distribution Plot', 'Count Plot']

        selected_plot = st.selectbox("Select a plot",options= plot_list, index =None)
        # we are using None as the default index because we want the user to select the plot type
        #We are using selection instead of selectbox because we can select multiple plots 

        st.write(x_axis)     
        st.write(y_axis) 
        st.write(selected_plot) 

        #button to generate the plots
        if st.button("Generate Plot"):
            fig, ax = plt.subplots(figsize=(6,4))
        
            if selected_plot == 'Line Plot':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)

            if selected_plot == 'Bar Plot':
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)

            if selected_plot == 'Scatter Plot':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
            

            if selected_plot == 'Distribution Plot':
                sns.histplot(x=df[x_axis], kde = True, ax=ax)
            

            if selected_plot == 'Count Plot':
                sns.countplot(x=df[x_axis], kde = True, ax=ax)

            #adjust the label sizes 

            ax.tick_params(axis='x', labelsize=10)
            ax.tick_params(axis='y', labelsize=10)

            #title axes labels
            plt.title(f'{selected_plot} of {y_axis} vs {x_axis}', fontsize=15)
            plt.xlabel(x_axis, fontsize=10)
            plt.ylabel(y_axis, fontsize=10)

            st.pyplot(fig)

        
            
