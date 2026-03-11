# Example Gradio application
import gradio as gr
import numpy as np

def greet(name, intensity):
    return f"Hello, {name}!" * intensity

# Create a simple interface
demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

# Run the demo
if __name__ == "__main__":
    demo.launch()