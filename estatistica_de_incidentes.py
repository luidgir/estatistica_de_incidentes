# Trabalho de conclusão da cadeira de Lógica de Programação do curso de Pós Graduação da Unifor
# Turma 8: Ciência de Dados @ 27/04/2024
# Grupo: Luidgi Machado Rôla        - Mat: 2419526
#        Josiane Freire do Vale     - Mat: 2417450
#        Francisco Sandro Tavares   - Mat: 2419976

# 
# O programa lê o arquivo (incidentes.csv) gerado a partir do GLPI com dados anonimizados, percorre o 
# arquivo e calcula a a quantidade de incidentes e o percentual de incidentes resolvidos e não resolvidos.
#

from pathlib import Path

caminho_do_arquivo=Path("incidentes.csv")

if caminho_do_arquivo.exists():
  print("O arquivo é valido!")
  # Inicia os contadores
  qt_incidente=0
  qt_incidente_solucionado=0
  qt_incidente_nao_solucionado=0
  
  # Abre o arquivo em modo leitura
  with open("incidentes.csv", 'r',encoding='utf-8') as arquivo: 
    for linha in arquivo:
      linha = linha.strip().split(',')
      
      # Verifica se o chamado foi solucionado
      if linha[7]=="SOLUCIONADO":
        qt_incidente_solucionado+=1
      else:
        qt_incidente_nao_solucionado+=1
      
      # Soma a quantidade de incidentes
      qt_incidente+=1
    
    # Resultado
    print(f"Quantidade de incidente: {qt_incidente}, solucionados: {qt_incidente_solucionado} e não solucionados: {qt_incidente_nao_solucionado}")
    print("Percentual de incidentes solucionados: {:.2f}%".format(qt_incidente_solucionado/qt_incidente*100))
    print("Percentual de incidentes não solucionados: {:.2f}%".format(qt_incidente_nao_solucionado/qt_incidente*100))

else:
  print("O arquivo não existe.")