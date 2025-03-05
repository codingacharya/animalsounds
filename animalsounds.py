import streamlit as st
from IPython.display import Audio
import os

# Function to play sound
def play_sound(sound_file):
    audio_path = os.path.join("sounds", sound_file)  # Assuming sounds are in 'sounds' folder
    return Audio(audio_path, autoplay=True)

# Dictionary of animals and their sound files
animals = {
    "Dog": ("dog.jpg", "dog.wav"),
    "Cat": ("cat.jpg", "cat.wav"),
    "Cow": ("cow.jpg", "cow.wav"),
    "Lion": ("lion.jpg", "lion.wav"),
    "Elephant": ("elephant.jpg", "elephant.wav"),
    "Horse": ("horse.jpg", "horse.wav")
}

# Dictionary of birds and their sound files
birds = {
    "Sparrow": ("sparrow.jpg", "sparrow.wav"),
    "Parrot": ("parrot.jpg", "parrot.wav"),
    "Eagle": ("eagle.jpg", "eagle.wav"),
    "Owl": ("owl.jpg", "owl.wav")
}

st.title("Animal and Bird Sounds App")

st.header("Animal Sounds")
for animal, (image, sound) in animals.items():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(image, width=100)
    with col2:
        if st.button(f"Play {animal} Sound"):
            st.audio(os.path.join("sounds", sound))

st.header("Bird Sounds")
for bird, (image, sound) in birds.items():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(image, width=100)
    with col2:
        if st.button(f"Play {bird} Sound"):
            st.audio(os.path.join("sounds", sound))
