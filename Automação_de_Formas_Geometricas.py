import pyautogui, time, math, keyboard # Bibliotecas para controle de mouse/teclado e cálculos matemáticos

def triangulo(t): 
    # Desenha um triângulo isósceles usando movimentos relativos (dragRel)
    metade = t / 2
    pyautogui.dragRel(t, 0, duration=1)          # Base
    pyautogui.dragRel(-metade, -t, duration=1)   # Sobe até o topo (metade da base para trás)
    pyautogui.dragRel(-metade, t, duration=1)    # Desce fechando no ponto inicial

def quadrado(t): 
    # Desenha um quadrado perfeito percorrendo os 4 lados com o tamanho 't'
    pyautogui.dragRel(t, 0, duration=1)   # Direita
    pyautogui.dragRel(0, -t, duration=1)  # Cima
    pyautogui.dragRel(-t, 0, duration=1)  # Esquerda
    pyautogui.dragRel(0, t, duration=1)   # Baixo

def circulo(raio): 
    # Pega a posição atual do mouse para servir de ponto central
    centro_x, centro_y = pyautogui.position()
    
    # Move para a borda do círculo antes de começar para não riscar o meio
    pyautogui.moveTo(centro_x + raio, centro_y, duration=1)
    time.sleep(1)
    
    # Loop de 1 a 365 graus para completar a volta
    for igraus in range(1, 366, 5):
        # Converte graus em radianos (o que o Python entende para calcular Seno e Cosseno)
        radiano = math.radians(igraus)
        
        # Fórmula matemática para encontrar os pontos X e Y da circunferência
        x = centro_x + raio * math.cos(radiano)
        y = centro_y + raio * math.sin(radiano)
        
        # Arrasta o mouse até a coordenada exata calculada
        pyautogui.dragTo(x, y)

def tamanho():
    # Abre uma caixa de confirmação para definir a escala do desenho
    resposta = pyautogui.confirm(text="Escolha o tamanho!", title='Tamanho', buttons=['100', '200', '300', '400'])
    # Converte o texto do botão para número inteiro. Padrão 200 se fechar a janela.
    return int(resposta) if resposta else 200

def escolher():
    # Menu principal interativo usando pop-ups do PyAutoGUI
    return pyautogui.confirm(text="Aoba, escolhe ai", title='Aoba', buttons=['Quadrado', 'Triangulo', 'Circulo', 'Sair'])

pyautogui.press('win')             # Abre o menu Iniciar
time.sleep(1)
pyautogui.write('Paint', interval=0.1) # Digita o nome do programa
time.sleep(1)
pyautogui.press('enter')           # Abre o Paint

# Loop principal do programa
while True:
    esc = escolher()   
    if esc:
        if esc != "Sair":
            valor_tamanho = tamanho()          # Pergunta o tamanho do desenho
            
        # Verifica qual opção foi clicada e executa a função correspondente
        match esc:
            case "Quadrado":
                time.sleep(3) # Tempo para o usuário posicionar o mouse na tela de desenho
                quadrado(valor_tamanho)
            case "Triangulo":
                time.sleep(3)
                triangulo(valor_tamanho)
            case "Circulo":
                time.sleep(3)
                circulo(valor_tamanho)
            case "Sair":
                exit() # Encerra o script
        
        time.sleep(0.1) # Pequena pausa para evitar sobrecarga do processador
