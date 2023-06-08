import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('ggplot')
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
import graphviz 
from sklearn import tree


def home_page():

    # Task 1:
    # Formatting the app for improved user experiance

    # Task 2: 
    # Add a page for CSV formatting from wdf

    # Task 3: 
    # Create general functions that can be used in each page when 
    # similar tasks are repeated (PCA, open file, etc.)
    
    # Look into OOP, & PEP 8

    st.markdown("Home page")
    st.sidebar.markdown("Home page")

    st.write("""
    The aim of this app is to process and plot a vibrational spectroscopy spectrum\n
    \n
    Index:\n
        Page 1: Formatting wdf file for CSV\n
        Page 2: Cumulative explained variance (CEV) plot\n
        Page 3: PC selection\n
        Page 4: Score plot\n
        Page 5: Loading plot
    """)


def page1():
    st.markdown("Page 1: CSV format check")
    st.sidebar.markdown("Page 1: CSV format check")
    
    st.write('''This page is to check that the csv file used in the next pages \n
    is in the correct format''')

def page2():

    # Task 1:
    # Have somthing print out the PCs representing a suitable ammount of variance
    # Potentially a method of setting a limit

    st.markdown("Page 2: CEV plot")
    st.sidebar.markdown("Page 2: CEV plot")

    st.write("""
    This page will plot the cumulative explained variance,
    indicating the number of principal components that relate
    to an acceptable ammount of variance within the dataset.
    """)

    dataframe0 = [] 
    uploaded_file0 = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
    
    if uploaded_file0 is not None:
        df0 = pd.read_csv(uploaded_file0)
          

        if len(df0) > 0:
            pca = PCA().fit(df0)

            CEV = pca.explained_variance_ratio_[0:15]
        
            fig0, ax0 = plt.subplots()
            ax0.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],np.cumsum(CEV))
            ax0.set_xlabel('number of components')
            ax0.set_ylabel('cumulative explained variance')
            ax0.set_title('Explained variance', fontsize = 10)
            ax0.grid(True)    

            st.write(fig0)

            FN = st.text_input("Save file: ")

            fig0.savefig('scatter.png') 

            if len(FN) > 0:
                fn = 'scatter.png'
                        
                with open(fn, "rb") as img:
                    btn = st.download_button(
                    label="Download image",
                    data=img,
                    file_name=str(FN),
                    mime="image/png") 

        Sel = st.text_input("What is the minimum variance you will allow? \n (typical value around 1%)")
        if len(Sel) > 0:
            Seltd = str(len(CEV[CEV > float(Sel)/100]))
            st.write("The first " + Seltd + " principal components are\n above your threshold of " + Sel + "%")


def page3():
    st.write("""
        Select the data matrix (X). 
        """)
    #dataframe = [] 
    uploaded_data = st.file_uploader('files_data', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
    
    

    if uploaded_data is not None:
        
        
        df = pd.read_csv(uploaded_data)
                
        transformer = PCA(n_components=8)
        columns = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8']
        X_pc = transformer.fit_transform(df)
        DF = pd.DataFrame(X_pc, columns = columns)
        
        st.write("""
            Select labels (y). 
            """)

        uploaded_labels = st.file_uploader('files_labels', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
        
        if uploaded_labels is not None:
            
            

            labels = pd.read_csv(uploaded_labels)

            decision_tree = DecisionTreeClassifier(random_state=0, max_depth=3)
            decision_tree = decision_tree.fit(DF, labels)
        
            fig = plt.figure(figsize=(25,20))
            _ = tree.plot_tree(decision_tree, feature_names=columns, filled=True)

            st.write(fig)

            FN = st.text_input("Save file: ")

            fig.savefig('scatter.png') 

            if len(FN) > 0:
                fn = 'scatter.png'
                        
                with open(fn, "rb") as img:
                    btn = st.download_button(
                    label="Download image",
                    data=img,
                    file_name=str(FN),
                    mime="image/png") 

            

    
def page4():

    # Task 1:
    # Build in a method of varying the number of classes

    st.markdown("Page 4: Score plot")
    st.sidebar.markdown("Page 4: Score plot")

    st.write("""
    The aim of this page is to plot two principal components 
    against ech other, showing their score plot. 
    """)
    First_pc = ''
    Second_pc = ''

    First_pc = st.text_input("First PC: ")
    Second_pc = st.text_input("Second PC: ")

    if len(First_pc) > 0 and len(Second_pc) > 0:
        #dataframe1 = [] 
        
        st.write("""
            Select data matrix (X) 
            """)

        uploaded_data1 = st.file_uploader('files1', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
        if uploaded_data1 is not None:
            df1 = pd.read_csv(uploaded_data1)
            
            

        
            if len(df1) > 0: 
                st.write("""
                Select labels (y)
                """)

                uploaded_labels1 = st.file_uploader('files2', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
                
                if uploaded_labels1 is not None:
                    ls = pd.read_csv(uploaded_labels1)

                    labels = np.array(ls)


                
              
                    transformer = PCA(n_components=8)
                    X_pc = transformer.fit_transform(df1)
                    DF = pd.DataFrame(X_pc, columns = ['1', '2','3', '4', '5', '6', '7', '8'])

                    PCs = pd.concat([DF[First_pc], DF[Second_pc]], axis=0)

                    positive_lim0 = round(float(max(abs(PCs))*1.2),2) 
                    negative_lim0 = round(float(max(abs(PCs))*-1.2),2)

                    fig1, ax1 = plt.subplots()
                    ax1.set_xlabel('Principal Component ' + str(First_pc), fontsize = 15)
                    ax1.set_ylabel('Principal Component ' + str(Second_pc), fontsize = 15)
                    ax1.set_title('2 component PCA', fontsize = 20)
                    ax1.set_ylim(negative_lim0,positive_lim0)
                    ax1.set_xlim(negative_lim0,positive_lim0)
            
                    targets = [np.unique(labels)[0], np.unique(labels)[1]]
                    colors = ['r','b']
                    for target, color in zip(targets,colors):
                        indicesToKeep = labels == target
                        ax1.scatter(DF.loc[indicesToKeep, str(First_pc)]
                            , DF.loc[indicesToKeep, str(Second_pc)]
                            , c = color
                            , s = 50)
                    ax1.legend(targets)
                    ax1.grid(True)

                    ax1.axhline(y = 0, color = 'k', linestyle = '--', alpha=0.5)
                    ax1.vlines(x=0, ymin=negative_lim0, ymax=positive_lim0, color = 'k', linestyle = '--', alpha=0.5)

                    st.write(fig1)

                    FN = st.text_input("Save file: ")

                    fig1.savefig('scatter.png') 

                    if len(FN) > 0:
                        fn = 'scatter.png'
                        
                        with open(fn, "rb") as img:
                            btn = st.download_button(
                            label="Download image",
                            data=img,
                            file_name=str(FN),
                            mime="image/png") 


def page5():

    # Task 1:
    # Add wavenumbers to the plot

    # Task 2:
    # Looking to include an automatic method for identifying
    # the top number of peaks, ideally using a slider
    
    st.markdown("Page 5: Loadings plots")
    st.sidebar.markdown("Page 5: Loadings plots")

    st.write('Loadings plot page')

    PC = ''
    
    PC = st.text_input("Principal component: ")
    
    if len(PC) > 0:
        
        uploaded_file2 = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
        if uploaded_file2 is not None:
            df2 = pd.read_csv(uploaded_file2)
            
         
            if len(df2) > 0:
                
                st.write("Do you want to add the corect spectral range?")

                uploaded_range = st.file_uploader('range', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
                
                if uploaded_range is not None:
                    rg = pd.read_csv(uploaded_range)

                    range = np.array(rg)

                    pca = PCA().fit(df2)
                    loadings = pca.components_.T
                    Loadings = pd.DataFrame(loadings)

                    PC_loading = np.array(Loadings.iloc[:,int(PC)])

                    positive_lim1 = round(float(max(abs(PC_loading))*1.1),2) 
                    negative_lim1 = round(float(max(abs(PC_loading))*-1.1),2) 

                    fig2, ax2 = plt.subplots()
                    ax2.plot(range, PC_loading) 
                    ax2.axhline(y = 0, color = 'k', linestyle = '--', alpha=0.5)
                    ax2.set_title('PC' + str(PC) + ' Loading plot')
                    ax2.set_ylim(negative_lim1,positive_lim1)
                    ax2.grid(True)

                    st.write(fig2) 


                    FN = st.text_input("Save file: ")

                    fig2.savefig('scatter.png') 

                    if len(FN) > 0:
                        fn = 'scatter.png'
                        
                        with open(fn, "rb") as img:
                            btn = st.download_button(
                            label="Download image",
                            data=img,
                            file_name=str(FN),
                            mime="image/png")

                else:
                    pca = PCA().fit(df2)
                    loadings = pca.components_.T
                    Loadings = pd.DataFrame(loadings)

                    PC_loading = np.array(Loadings.iloc[:,int(PC)])

                    positive_lim1 = round(float(max(abs(PC_loading))*1.1),2) 
                    negative_lim1 = round(float(max(abs(PC_loading))*-1.1),2) 

                    fig2, ax2 = plt.subplots()
                    ax2.plot(PC_loading) 
                    ax2.axhline(y = 0, color = 'k', linestyle = '--', alpha=0.5)
                    ax2.set_title('PC' + str(PC) + ' Loading plot')
                    ax2.set_ylim(negative_lim1,positive_lim1)
                    ax2.grid(True)

                    st.write(fig2)

                    

                    FN = st.text_input("Save file: ")

                    fig2.savefig('scatter.png') 

                    if len(FN) > 0:
                        fn = 'scatter.png'
                        
                        with open(fn, "rb") as img:
                            btn = st.download_button(
                            label="Download image",
                            data=img,
                            file_name=str(FN),
                            mime="image/png")   


page_names_to_funcs = {  

    "Home Page": home_page,
    "Page 1 (CSV format)": page1,
    "Page 2 (CEV plot)": page2, 
    "Page 3 (PC select)": page3,
    "Page 4 (Score plot)": page4, # Could add a plotly 3D score plot
    "Page 5 (Loading plot)": page5,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()