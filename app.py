import streamlit as st
import os
import json
import re

# Configuração da página
st.set_page_config(
    page_title="40 Orações do Arcanjo Gabriel - Inspiradas por Padre Cícero",
    page_icon="✨",
    layout="wide",
)

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f4f4;
        color: #333;
    }
    h1 {
        color: #4A90E2;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.5rem;
    }
    h2 {
        color: #4A90E2;
        font-family: 'Georgia', serif;
        font-size: 1.8rem;
    }
    .stButton button {
        background-color: #4A90E2;
        color: white;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 18px;
        font-family: 'Georgia', serif;
        width: 100%;
    }
    .stVideo {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
    }
    .stDownloadButton button {
        background-color: #FF0000;
        color: white;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 18px;
        font-family: 'Georgia', serif;
        width: 100%;
    }
    .center-image {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem;
        }
        h2 {
            font-size: 1.5rem;
        }
        .stButton button, .stDownloadButton button {
            padding: 12px 24px;
            font-size: 16px;
        }
        .stVideo {
            max-width: 100%;
        }
    }
    .loading-message {
        font-size: 0.9rem;
        color: #666;
        text-align: center;
        margin-bottom: 20px;
    }
    .final-message {
        text-align: center;
        margin-top: 30px;
        font-size: 1.1rem;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Imagem de topo
st.markdown('<div class="center-image">', unsafe_allow_html=True)
st.image("sao_miguel.jpg", width=100)
st.markdown('</div>', unsafe_allow_html=True)

# Título
st.title("40 Orações do Arcanjo Gabriel - Inspiradas por Padre Cícero")
st.markdown("---")


# Função para extrair número corretamente
def extrair_numero(nome_arquivo):
    match = re.search(r"(\d+)", nome_arquivo)
    return int(match.group(1)) if match else float('inf')


# Cache do vídeo
@st.cache_data
def load_video(video_path):
    with open(video_path, "rb") as file:
        return file.read()


# Carregar descrições
descricoes = {}
if os.path.exists("descricoes.json"):
    with open("descricoes.json", "r", encoding="utf-8") as f:
        descricoes = json.load(f)

# Lista de vídeos
videos = sorted(
    [f for f in os.listdir() if f.lower().endswith(".mp4")],
    key=extrair_numero
)

# Exibir vídeos
if not videos:
    st.error("Nenhum vídeo encontrado na pasta atual.")
else:
    st.write("### Escolha uma oração para assistir:")
    st.markdown('<div class="loading-message">Aguarde alguns segundos para carregar os vídeos...</div>',
                unsafe_allow_html=True)

    for index, video in enumerate(videos, start=1):
        nome_exibicao = f"Oração {index:02d}"
        st.write(f"**{nome_exibicao}**")

        if video in descricoes:
            st.write(descricoes[video])

        video_data = load_video(video)
        st.video(video_data, format="video/mp4", start_time=0)

        with open(video, "rb") as file:
            st.download_button(
                label=f"Baixar {nome_exibicao}",
                data=file,
                file_name=video,
                mime="video/mp4",
                key=f"download_{video}",
            )

        if index == len(videos):
            st.markdown("---")
            st.markdown(
                """
                <div class="final-message">
                    <p>Acesse aqui as 40 Orações mais Poderosas de Arcanjo Miguel, rezadas por FREI GILSON! ➡️ 
                    <a href="https://lastlink.com/p/CEB3A8A56/checkout-payment/" target="_blank">Clique Aqui</a></p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown("---")
