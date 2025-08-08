import requests

def get_github_users(since=0, per_page=10):
    """
    Obtém usuários da API do GitHub.
    since -> ID a partir do qual buscar usuários
    per_page -> número de usuários por página (máximo 100)
    """
    url = f"https://api.github.com/users?since={since}&per_page={per_page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao acessar a API:", response.status_code)
        return []

def bubble_sort(data, key):
    """
    Ordena usando o algoritmo Bubble Sort baseado na chave fornecida.
    key -> função que extrai o valor para comparação
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(data[j]) > key(data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    return data


usuarios = get_github_users(per_page=10)


for usuario in usuarios:
    detalhes = requests.get(usuario["url"]).json()
    usuario["followers"] = detalhes.get("followers", 0)


usuarios_ordenados = bubble_sort(usuarios, key=lambda u: u["followers"])


for u in usuarios_ordenados:
    print(f"{u['login']} - Seguidores: {u['followers']}")