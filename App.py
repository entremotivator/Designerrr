import streamlit as st
import aggdraw
from PIL import Image, ImageDraw

# Function to draw a square
def draw_square(draw, color_choice):
    width, height = draw.bitmap.width, draw.bitmap.height
    square_size = int(min(width, height) * 0.8)
    square_position = ((width - square_size) // 2, (height - square_size) // 2)
    square_end_position = (square_position[0] + square_size, square_position[1] + square_size)

    draw.rectangle([square_position, square_end_position], fill=color_choice)

# Streamlit app layout
st.title("Drawing Layers with aggdraw")

# Sidebar for user input
num_layers = st.sidebar.number_input("Number of Layers", min_value=1, max_value=5, value=1, step=1)

# Create a blank image
width, height = 500, 500
combined_image = Image.new("RGB", (width, height), "white")

# Draw based on user input
for layer in range(num_layers):
    st.sidebar.markdown(f"### Layer {layer + 1}")
    shape_choice = st.sidebar.selectbox(f"Select Shape for Layer {layer + 1}", ["circle", "square"])
    color_choice = st.sidebar.color_picker(f"Choose Color for Layer {layer + 1}")

    draw = aggdraw.Draw(combined_image)
    
    if shape_choice == "circle":
        draw.ellipse([50, 50, width - 50, height - 50], fill=color_choice)
    elif shape_choice == "square":
        draw_square(draw, color_choice)

    draw.flush()

# Display the combined image
st.image(combined_image, use_column_width=True)

# Save combined image
if st.button("Save Combined Image"):
    combined_image.save("combined_image.png")
    st.success("Image saved successfully!")

# Close Streamlit app on exit
if st.button("Exit"):
    st.balloons()
    st.stop()
