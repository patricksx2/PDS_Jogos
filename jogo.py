import forca
import adivinhacao
      
  def escolhe_jogo():
      print("*******************************")
      print("*******Escolha seu jogo!*******")
      print("*******************************")
          
          
      print("(1)  forca  (2)  adivinhação ")
          
      jogo = int(intup("qual jogo? "))
          
      if(jogo == 1):
      print("jogando forca")
      forca.jogar()
      elif(jogo == 2):
      print("jogando adivinhação") 
      adivinhacao.jogar()
      
      if(__name__ == "__main__"):
          escolhe_jogo()

          
          
          
          
          
          
          
          
          
          