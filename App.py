import streamlit as st
import turtle
from PIL import Image
import os

# Function to draw a square using Turtle
def draw_square(turtle_instance):
    for _ in range(4):
        turtle_instance.forward(100)
        turtle_instance.right(90)

# Streamlit app layout
st.title("Turtle Image Design App")
st.sidebar.title("Options")

# Sidebar for user input
num_images = st.sidebar.number_input("Number of Images", min_value=1, max_value=5, value=1, step=1)

# Initialize Turtle instances for each image
turtles = [turtle.Turtle() for _ in range(num_images)]

# Draw based on user input
for idx, turtle_instance in enumerate(turtles):
    st.sidebar.markdown(f"### Image {idx + 1}")

    shape_choice = st.sidebar.selectbox(f"Select Shape for Image {idx + 1}", ["turtle", "circle", "square"])
    user_image = st.sidebar.file_uploader(f"Upload Image {idx + 1}", type=["jpg", "jpeg", "png"])

    if user_image is not None:
        st.sidebar.image(user_image, caption=f"Uploaded Image {idx + 1}", use_column_width=True)

        # Set Turtle shape
        turtle_instance.shape(shape_choice)

        # Draw layer on the image
        if st.sidebar.button(f"Add Layer for Image {idx + 1}"):
            draw_square(turtle_instance)

# Save combined image
if st.button("Save Combined Image"):
    combined_canvas = turtle.Screen()
    
    for idx, turtle_instance in enumerate(turtles):
        # Get turtle canvas as an image
        turtle_instance_canvas = turtle_instance.getcanvas()
        turtle_instance_canvas.postscript(file=f"temp_image_{idx}.eps", colormode='color')
        Image.open(f"temp_image_{idx}.eps").save(f"temp_image_{idx}.png", "png")

        # Clear the canvas
        turtle_instance.reset()

    combined_canvas.bye()

    # Combine images using PIL
    combined_image = None
    for idx in range(num_images):
        img_path = f"temp_image_{idx}.png"
        if os.path.exists(img_path):
            img = Image.open(img_path)
            if combined_image is None:
                combined_image = img
            else:
                combined_image.paste(img, (0, 0), img)

    if combined_image is not None:
        combined_image.save("combined_image.png", "png")
        st.success("Images saved and combined successfully!")

# Close Turtle graphics on Streamlit exit
if st.button("Exit"):
    st.balloons()
    st.stop()
