from pytube import YouTube

# ENTRADA DO LINK DO VÍDEO
link = str(input("DIGITE O LINK QUE VOCÊ DESEJA BAIXAR: "))

# DIRETÓRIO EM QUE O VÍDEO VAI SER BAIXADO
user = str(input("DIGITE O NOME DO SEU USUÁRIO NO COMPUTADOR: "))
path = f"/Users/{user}/Downloads/"

# VÍDEO NO YOUTUBE
yt = YouTube(link)

# INFORMAÇÕES DO VÍDEO
print(f"TÍTULO DO VÍDEO: {yt.title}")
print(f"NÚMERO DE VIEWS: {yt.views}")
print(f"DURAÇÃO DO VÍDEO: {yt.length}")
print(f"CANAL: {yt.author}")
# print(f"AVALIAÇÃO DO VÍDEO: {yt.rating}")

# PEGANDO A MELHOR RESOLUÇÃO
videoDownload = yt.streams.get_highest_resolution()

# BAIXANDO O VÍDEO
print("BAIXANDO...")
videoDownload.download(path)
print("DOWNLOAD CONCLUÍDO!")
