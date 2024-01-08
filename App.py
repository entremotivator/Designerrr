import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import io

# Function to draw a square
def draw_square(ax, color_choice):
    ax.add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.8, color=color_choice, alpha=0.5))

# Streamlit app layout
st.title("Drawing Layers with Matplotlib")

# Sidebar for user input
num_layers = st.sidebar.number_input("Number of Layers", min_value=1, max_value=5, value=1, step=1)

# Draw based on user input
fig, ax = plt.subplots()

for layer in range(num_layers):
    st.sidebar.markdown(f"### Layer {layer + 1}")
    shape_choice = st.sidebar.selectbox(f"Select Shape for Layer {layer + 1}", ["circle", "square"])
    color_choice = st.sidebar.color_picker(f"Choose Color for Layer {layer + 1}")

    if shape_choice == "circle":
        ax.add_patch(plt.Circle((0.5, 0.5), 0.4, color=color_choice, alpha=0.5))
    elif shape_choice == "square":
        draw_square(ax, color_choice)

# Display the plot
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')

# Save combined image
if st.button("Save Combined Image"):
    # Save the figure to a BytesIO buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Open the image using PIL and save it
    img = Image.open(buf)
    img.save("combined_image.png")
    st.success("Image saved successfully!")

# Display the plot in Streamlit
st.image("combined_image.png", use_column_width=True)

# Close Matplotlib graphics on Streamlit exit
if st.button("Exit"):
    plt.close()
    st.balloons()
