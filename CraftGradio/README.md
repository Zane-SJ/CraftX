# CraftGradio

This is a Gradio application for large model learning and experimentation.

## Setup

1. Navigate to the CraftGradio directory:
   ```
   cd d:\workspace\CraftX\CraftGradio
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Gradio application:

```
cd src
python app.py
```

The application will be available at `http://localhost:7860` by default.

## Project Structure

- `requirements.txt`: Contains all the Python dependencies
- `src/app.py`: Main Gradio application file
- `src/`: Directory for source code files