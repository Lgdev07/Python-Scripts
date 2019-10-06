
class Musica():
    def __init__(self, titulo, autor, estilo):
        self._titulo = titulo
        self._autor = autor
        self._estilo = estilo
    
    def __str__(self):
        return self._titulo

    def alter_titulo(self, novo_titulo):
        self._titulo = novo_titulo

class Estilos():
    def __init__(self, ritmo):
        self._ritmo = ritmo
    
        

musica1 = Musica('titulo1', 'luan')

print(musica1)

musica1.alter_titulo('novo_titulo_haha')

print(musica1)