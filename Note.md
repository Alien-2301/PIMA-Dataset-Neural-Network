Running Local server: `streamlit run streamlit_app.py`

##### why python streamlit_app.py does not work? 
Typing python causes the device to execute the script line by line (in top to bottom order). It runs from top to bottom, then exit. 

### Q.2 Data Flow 
Streamlit archicture allows the app to be written similarly to python scripts. however,the streamlitapps have unique data flow, in which, streamlit reruns your entire updated python script from top to bottom in order to update on the webpage. 

### Q.3 Two Distict ways. of displaying data

#### st.write(*args, unsafe_allow_html=False)
The function that performs differently based on the different arguments. The commonly used method is the using string argument type which leads to the st.markdown(). It can be used to display other data types such as dataframe, function() and keras model (which the latter will be used to display the models in the project). 

#### Magic
Streamlit uses magic commands, which allowss developer to write variable without explcit usage of st.write in order to display the variables. 

### Q.4 Development flow / “Always rerun”
1. **Save the Source File**
   - Save your code whenever you make changes to your Streamlit app.

2. **Rerun the App**
   - Streamlit detects changes to the source file.
   - Select **"Always rerun"** at the top-right to automatically update the app after saving.

3. **Use an Interactive Development Loop**
   - Write or modify code.
   - Save the source file.
   - View and test the updated app.
   - Repeat until satisfied with the results.

4. **Key Benefit**
   - Streamlit makes development faster by allowing you to see and test code changes immediately.


### @st.cache_resource
The app uses the same model unless 
- replaces the model.keras
- clear caches
- restart app

#### @st.cache_data vs @st.cache_resource
- st.cache_data is used for serializable data (e.g. Pandas df, lists and dicts). It returns safe copies
- st.cache_resource is for global unserializable singletons. 
