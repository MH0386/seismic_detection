import requests

import streamlit as st

st.set_page_config(
    page_title="Chat with Napoleon Bonaparte",
    page_icon="😀",
    layout="wide",
)


def request_prediction(query: str):
    with st.status("Downloading data...", expanded=True) as status:
        st.write("Checking is the Chatacter alive")
        response = requests.get(f"{CONFIG['api']['localhost']}/", timeout=100)
        print(response)
        if response["status"] == "ok":
            st.write("Chatacter is alive")
        else:
            st.write("Chatacter is not alive")
        st.write("Chatacter is thinking")
        response_text = requests.post(
            f"{CONFIG['api']['localhost']}/get_text?query='{query}'",
        )
        st.write("Chatacter is generating the audio file")
        response_audio = requests.post(
            f"{CONFIG['api']['localhost']}/get_audio?query='{response_text}'"
        )
        st.write("Chatacter is generating the video file")
        response_video = requests.post(f"{CONFIG['api']['localhost']}/get_video")
        print(response_video)
        status.update(label="Download complete!", state="complete", expanded=False)
    return response


st.title("😎 Chat with Napoleon Bonaparte")
user_input = st.chat_input("Type your message here")

if user_input is not None:
    message = st.chat_message("human")
    message.write("🕒")
    response, audio = request_prediction(user_input)
    message.write(response)
    st.audio(audio, format="audio/wav")