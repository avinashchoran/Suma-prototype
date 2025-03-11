# Suma - Elevating Your Learning Experience

Suma is an innovative application designed to transform your handwritten notes into digital format, summarize content, and convert text to speech for an enhanced learning experience.

## 🌟 Features

### 📝 Digital Note Conversion
- Upload handwritten notes
- Process and convert to digital text

### 📊 Summarization
- **Basic Summarization**: Create concise summaries using LSA (Latent Semantic Analysis)
- **Advanced Summarization**: Generate more nuanced summaries using BART AI model
- Customize summary length with intuitive controls

### 🔊 Audio Conversion
- Convert both full notes and summaries to audio
- Listen to your study material on the go
- Playback controls (start, pause, resume)

## 🛠️ Technologies Used

- **Frontend**: CustomTkinter (enhanced Tkinter for modern UI)
- **Text Processing**: 
  - Sumy for LSA summarization
  - HuggingFace Transformers (BART) for advanced AI summarization
- **Audio**: 
  - GTTS (Google Text-to-Speech)
  - Pygame for audio playback
- **Web Scraping** (for future OCR implementation):
  - Selenium
  - Beautiful Soup

## 📋 Prerequisites

- Python 3.8+
- Chrome WebDriver (for planned OCR functionality)

## 🔧 Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/suma.git
   cd suma
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Download the BART model (will be downloaded automatically on first run):
   ```
   # No manual step needed - the model will be downloaded when first used
   ```

## 📖 Usage

1. Launch the application:
   ```
   python suma.py
   ```

2. **Upload Notes**:
   - Click "Open" to select a file
   - Click "Process" to convert to digital text
   
3. **Create Summaries**:
   - Click "Summarize" for basic summarization
   - Click "Advanced Summarize" for AI-powered summaries
   - Use "+" and "-" buttons to adjust summary length

4. **Listen to Notes**:
   - Click "Start with digital notes" to listen to the full text
   - Click "Start with summarized notes" to listen to the summary
   - Use "Pause" and "Resume" to control playback

## 🚀 Future Development

- Implement direct OCR (Optical Character Recognition) for handwritten notes
- Add support for multiple languages
- Create a cloud-based version for mobile access
- Implement note organization and tagging system

## 🙏 Acknowledgements

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern UI components
- [Sumy](https://github.com/miso-belica/sumy) for text summarization
- [HuggingFace Transformers](https://github.com/huggingface/transformers) for advanced AI models