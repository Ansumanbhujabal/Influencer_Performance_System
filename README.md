# Influencer Performance System

A resource-intensive project designed to process video data, cluster influencers, and generate performance insights, using OpenAI's CLIP model for embeddings, facial recognition, and clustering techniques.

---

## **Architecture Overview**

1. **Input:**
   - Video URLs provided as raw data.
  
2. **Output:**
   - Generate a comprehensive report showcasing influencers’ performance with clustered data, visualizations, and insights.
   - **See The full output**
     [Influencer Performance System](https://influencerperformancesystemansumanbhujabala.streamlit.app/)
     ## Influencer Performance Report


| Influencer Label | Influencer Pic                                                                                                   | Average Performance | Video URL                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------|
| 30               | ![Influencer 30](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/32/man_frame_1.jpg) | 1.5304             | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-604041931565137)                |
| 25               | ![Influencer 25](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/27/man_frame_17.jpg) | 1.12256666666667   | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-925260332281638)                |
| 3                | ![Influencer 3](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/3/man_frame_3.jpg) | 1.02478604992305   | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-992064161877405)                |
| 55               | ![Influencer 55](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/58/man_frame_21.jpg) | 0.9830456907       | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-817763467176157)                |
| 45               | ![Influencer 45](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/48/man_frame_1.jpg) | 0.917806254725     | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-883738210384679)                |
| 15               | ![Influencer 15](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/17/man_frame_3.jpg) | 0.8273821321       | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-954832972830686)                |
| 7                | ![Influencer 7](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/7/woman_frame_23.jpg) | 0.80381331575      | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-987643572956494)                |
| 22               | ![Influencer 22](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/24/man_frame_17.jpg) | 0.7929559845       | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-932703258597949)                |
| 34               | ![Influencer 34](https://raw.githubusercontent.com/Ansumanbhujabal/Influencer_Performance_System/main/influencers/detected_objects_archive/36/man_frame_17.jpg) | 0.5907609883       | [Video Link](https://fgimagestorage.blob.core.windows.net/facebook-assets/hd-905739711170399)                |


3. **Process Flow:**
   - Generate vector embeddings for each video using OpenAI CLIP.
   - Cluster videos based on their embeddings to identify unique videos.
   - Calculate the average performance score for each unique video.
   - Extract human faces from the videos using OpenCV Haar cascades.
   - Identify the best-captured face from extracted images.
   - Save images to a GitHub raw content repository.
   - Match influencer faces across clusters to combine clusters based on face similarity using OpenAI CLIP.
   - Calculate the average performance score for each unique influencer.
  
     ![diagram-export-12-1-2024-9_08_38-PM](https://github.com/user-attachments/assets/ccd36bc4-06c3-42e5-b580-2d44cd4d9d35)




4. **Visualization:**
   - Accessible via a Streamlit app or as an HTML file.

---

## **System Used**

### **Machine Specifications:**
- **CPU:** 4 vCPUs (Intel Xeon Scalable, 3.5 GHz, Sapphire Rapids)
- **Memory:** 16 GiB (4 GiB per vCPU)
- **Operating System:** x86_64 architecture
- **Environment:** LightningAI equivalent system

### **Dependencies:**
All dependencies are listed in the `requirements.txt` file.

---

## **Setup Guide**

### **Clone the Repository**
```bash
git clone https://github.com/Ansumanbhujabal/Influencer_Performance_System.git
cd Influencer_Performance_System
```

### **Create and Activate Virtual Environment**
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
```

### **Install Dependencies**
Install all required packages:
```bash
pip install -r requirements.txt
```

Manually install additional dependencies:
```bash
pip install ftfy regex tqdm --quiet
pip install git+https://github.com/openai/CLIP.git --quiet
pip install matplotlib --quiet
pip install opencv-python-headless --quiet
pip install torch torchvision torchaudio --quiet
```

### **Run the Jupyter Notebook**
1. Navigate to the `notebooks` directory:
   ```bash
   cd notebooks
   ```
2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Open and run `Data_Processor_and_Insights.ipynb` to process the data and generate insights.

---

## **Visualization and Report Access**

### **Online Access:**
The performance report can be visualized remotely:
- [Influencer Performance System](https://influencerperformancesystemansumanbhujabala.streamlit.app/)

### **Local Access:**
1. Open The HTML file present in any browser
   ```bash
   influencer_report_up.html
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. For Numbers , you can refer to the 
   ```bash
   cd /output
   Final_Influencer_Data_insights_up_dec1_t2.xlsx
   ```
3. Open the generated report in any browser.

---

## **Future Scope**
- **Real-time Face Matching:** Optimize the workflow by introducing real-time face extraction and matching, eliminating redundant processes to save resources and reduce execution time.
- **Enhanced Clustering:** Improve clustering mechanisms for better influencer detection and performance accuracy.
- **Scalability:** Adapt the system to process larger datasets more efficiently.

---

## **Challenges Faced**
- **Resource-Intensive Processing:** Managing vector generation, face matching, and clustering on non-GPU systems.
- **Data Cleaning:** Ensuring unique identification of videos and influencers from raw, unstructured data.
- **Cluster Matching:** Efficiently combining clusters to avoid duplicates while maintaining accuracy.

---

## **Made Over a Weekend**
Created with passion and dedication in a short span to showcase influencer performance analytics.

---

**Author**: [Ansuman Bhujabal](https://github.com/Ansumanbhujabal)  
**GitHub Repository**: [Influencer Performance System](https://github.com/Ansumanbhujabal/Influencer_Performance_System)  
