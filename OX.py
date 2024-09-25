###########################################
#  _______      _______    _____________  #               
#  \      \    /      /   |   _______   | #  
#   \      \  /      /    |  |       |  | #  
#    \      \/      /     |  |       |  | #
#    /      /\      \     |  |       |  | #
#   /      /  \      \    |  |_______|  | #
#  /______/    \______\   |_____________| #                   
#                                         # 
###########################################

import time
import pygame
import random

pygame.init()

# запись цветов интерфейса
white = (250, 235, 215)
dark_white=(255, 222, 173) 
black = (0, 0, 0)
red = (255, 0, 0)
dark_red = (139, 0, 0)
green = (0, 100, 0)
FireBrick=(178, 34, 34)
DarkOrange=(255, 140, 0)
GreenYellow=(176, 224, 230)
brown=(34, 139, 34)

# размеры поля    
dis_x=905
dis_y=dis_x
dis=pygame.display.set_mode((dis_x,dis_y)) # создаем игровое поле
size=40
ch=0

# подготовка дисплея и запуск времени
pygame.display.update() # обновляем экран
pygame.display.set_caption('OX')
clock=pygame.time.Clock()
txt_style=pygame.font.SysFont(None,40) # задание размера текста

def mapa(): # рисует поле
    
    for i in range (2,dis_x,100):
        pygame.draw.line(dis,dark_white,(i,0),(i,dis_y),2)
        pygame.draw.line(dis,dark_white,(0,i),(dis_x,i),2)
    for i in range (2,dis_x,300):
        pygame.draw.line(dis,dark_white,(i,0),(i,dis_y),5)
        pygame.draw.line(dis,dark_white,(0,i),(dis_x,i),5)    

def pause(): # пишет пауза
   value = txt_style.render("Pause" , True, black)
   dis.blit(value, [0, 0]) 

def massage(text,color): # функция выводящая сообщение
    msg=txt_style.render(text,True,color)
    dis.blit(msg,[dis_x/2-len(text)*6,dis_y/2-20])

def draw_dot(size,dot_list,cordsi,cords): # рисует точки доставая из тапла dot_list их координаты и значения цвета
    
    for i in dot_list:
        if i[2]%2==0:
            pygame.draw.rect(dis, brown, [i[0]-size/2+5,i[1]-size/2+5,size,size])
        else:
            pygame.draw.rect(dis, red, [i[0]-size/2+5,i[1]-size/2+5,size,size])   

def gameloop():
    gr=True #  флаг отвечающий за определение победившего цвета, по умолчанию считается, что зеленые выйграли.
    draw=False
    ###################################################################################################################################################
    # матрицы Ака подложка
    inmatrix=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix1=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix2=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix3=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix4=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix5=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix6=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix7=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix8=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    inmatrix9=[[5,6,7],
              [8,9,10],
              [11,13,14]] 
    
    # координаты зеленой подсветки
    global grx 
    global gry
    grx=0
    gry=0
    
    # координаты поставленой точки
    global cords
    cords=((0,0))
    cordsi=((0,0)) # дополнительная переменная для отсеивания невозможных нажатий 
    
    global count
    count=0

    game_end=False # флаг отвечающий за конец игры
    game_close=False # стартовое меню
    fl=True # флаг отвечающий за первый ход, вырубает обязанность ходить в зелёные поля
    Pause=False # флаг для октивации паузы
    timer=False # флаг для того чтобы тапл с точками не пополнялся постоянно, а только тогда когда было сделан клик мышью
    grfl=True
    rule=False
    # флаги для определения выйгранной клетки
    Win1=False
    Win2=False
    Win3=False
    Win4=False
    Win5=False
    Win6=False
    Win7=False
    Win8=False
    Win9=False
    # флаги для сохранения цвета выйгранной клетки
    win1=True
    win2=True
    win3=True
    win4=True
    win5=True
    win6=True
    win7=True
    win8=True
    win9=True
    # флаги для отключения смены координта выйгранной клетки
    fl1=True
    fl2=True
    fl3=True
    fl4=True
    fl5=True
    fl6=True
    fl7=True
    fl8=True
    fl9=True

    # массивы для определения координаты выйгранной клетки, если зеленый квадрат попадает в них, то вырубает обязанность ходить в зелёные поля
    mas1=((-1000,-1000))
    mas2=((-1000,-1000))
    mas3=((-1000,-1000))
    mas4=((-1000,-1000))
    mas5=((-1000,-1000))
    mas6=((-1000,-1000))
    mas7=((-1000,-1000))
    mas8=((-1000,-1000))
    mas9=((-1000,-1000))
    
    dot_list=[] # тапл с точками
    today_dot=[-1,-1,-1] # тапл для записи последней поставленной точки
    ptoday_dot=[-1,-1,-1]
    today_mas=[-1]
    ch=0 # переменная, от четности которой зависит цвет поставленной точки
    
    ###################################################################################################################################################
    
    while not game_end: # главный цикл, пока gama_end=False, игра продолжается
        rule=False
        grfl=True
        mapa()
        if Pause: # цикл экрана меню
            pygame.display.update()
        while Pause==True:
            dis.fill(white)
            massage('Press A to continue game', black)
            pause()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a: # запуск новой игры
                        Pause=False
                if event.type==pygame.QUIT: # закрытие окна
                    pygame.quit() # деинициализация библиотеки
                    quit()
        if game_close: # цикл экрана меню
            dis.fill(white)
            if gr==True and draw==False:
                massage('green wins', green)
            elif gr==False and draw==False:
                massage('red wins', red)  
            else:
                massage('draw', black)
            pygame.display.update()
            time.sleep(2)
        while game_close==True:
            dis.fill(white)
            massage('Press A to start game', black)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a: # запуск новой игры
                        gameloop()
                if event.type==pygame.QUIT: # закрытие окна
                    pygame.quit() # деинициализация библиотеки
                    quit() 
        for event in pygame.event.get(): # достаём все события из массива событий в библиотеке pygame. event.get() возвращает в терминал все события, которые происходят с игрой
            if event.type==pygame.QUIT: # закрытие окна
                pygame.quit() # деинициализация библиотеки
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE: 
                        Pause=True
                if event.key==pygame.K_r: 
                    game_close=True    

        ###################################################################################################################################################        
                
               

        ###################################################################################################################################################  

            if event.type==pygame.MOUSEBUTTONDOWN: # отслеживание нажатия мыши
                cordsi=event.pos # предварительная запись координат клика
                for i in dot_list:
                    if i[0]-50<=cordsi[0]<=i[0]+50 and i[1]-50<=cordsi[1]<=i[1]+50: 
                        count+=1
                if (mas1[0]<=cordsi[0]<=mas1[0]+300 and mas1[1]<=cordsi[1]<=mas1[1]+300) or (mas2[0]<=cordsi[0]<=mas2[0]+300 and mas2[1]<=cordsi[1]<=mas2[1]+300) or (mas3[0]<=cordsi[0]<=mas3[0]+300 and mas3[1]<=cordsi[1]<=mas3[1]+300) or (mas4[0]<=cordsi[0]<=mas4[0]+300 and mas4[1]<=cordsi[1]<=mas4[1]+300) or (mas5[0]<=cordsi[0]<=mas5[0]+300 and mas5[1]<=cordsi[1]<=mas5[1]+300) or (mas6[0]<=cordsi[0]<=mas6[0]+300 and mas6[1]<=cordsi[1]<=mas6[1]+300) or (mas7[0]<=cordsi[0]<=mas7[0]+300 and mas7[1]<=cordsi[1]<=mas7[1]+300) or (mas8[0]<=cordsi[0]<=mas8[0]+300 and mas8[1]<=cordsi[1]<=mas8[1]+300) or (mas9[0]<=cordsi[0]<=mas9[0]+300 and mas9[1]<=cordsi[1]<=mas9[1]+300):
                    count+=1
                     
                if count>0:
                    grfl=False
                    rule=False
                    count=0
                else:
                    grfl=True
                    rule=True        
                       
                
                # то самое легендарное условие необходимости ходить в зелёные поля, с кучей исключений)
                if rule==True and grx<=cordsi[0]<=grx+300 and gry<=cordsi[1]<=gry+300  or fl==True or (grx==mas1[0] and gry==mas1[1]) or (grx==mas2[0] and gry==mas2[1]) or (grx==mas3[0] and gry==mas3[1]) or (grx==mas4[0] and gry==mas4[1]) or (grx==mas5[0] and gry==mas5[1]) or (grx==mas6[0] and gry==mas6[1]) or (grx==mas7[0] and gry==mas7[1]) or (grx==mas8[0] and gry==mas8[1]) or (grx==mas9[0] and gry==mas9[1]):
                    cords=cordsi # после пройденной проверки коректности хода, записываем координатц нажатия мыши
                    fl=False # отключаем условие первого хода
                    timer=True # включаем таймер чтобы dot_list смог записать значение текущей точки
                    ch=ch+1 # смена цвета 
                     
        
        ###################################################################################################################################################

        # цикл определяющий в какой клетке был произведен клик мышью,"Поиск по диагоналям"
        for i in range(0,dis_x,100):
            for j in range(-9,8):    
                if (i+j*100)<cords[0]<=(i+(j+1)*100) and (i-100)<=cords[1]<=i and timer==True and rule==True:
                    # Если координата мыши находится в проверяем клетке:
                    today_dot=[] # обнуляем текущую точку
                    ptoday_dot=[]
                    # записываем текущую точку координаты x и y и текущий цвет
                    ptoday_dot=today_dot
                    today_dot.append(i+j*100+50) 
                    today_dot.append(i-50)
                    today_dot.append(ch)
                    # запихиваем текущую точку в тапл ко всем
                    dot_list.append(today_dot)  
                    ########################################################################################################################################
                    # заполнение подложек в виде матриц
                    for i in range (0,300,100):
                        for j in range (0,300,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix1[j//100][i//100]=2
                                else:
                                    inmatrix1[j//100][i//100]=1 
                                
                    
                    for i in range (0,300,100):
                        for j in range (300,600,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix4[(j-300)//100][i//100]=2
                                else:
                                    inmatrix4[(j-300)//100][i//100]=1 
                                

                    for i in range (0,300,100):
                        for j in range (600,900,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix7[(j-600)//100][i//100]=2
                                else:
                                    inmatrix7[(j-600)//100][i//100]=1 
                                  

                    for i in range (300,600,100):
                        for j in range (0,300,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix2[j//100][(i-300)//100]=2
                                else:
                                    inmatrix2[j//100][(i-300)//100]=1 
                                
                    
                    for i in range (300,600,100):
                        for j in range (300,600,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix5[(j-300)//100][(i-300)//100]=2
                                else:
                                    inmatrix5[(j-300)//100][(i-300)//100]=1 
                                

                    for i in range (300,600,100):
                        for j in range (600,900,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix8[(j-600)//100][(i-300)//100]=2
                                else:
                                    inmatrix8[(j-600)//100][(i-300)//100]=1 
                                

                    for i in range (600,900,100):
                        for j in range (0,300,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix3[j//100][(i-600)//100]=2
                                else:
                                    inmatrix3[j//100][(i-600)//100]=1 
                                
                    
                    for i in range (600,900,100):
                        for j in range (300,600,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix6[(j-300)//100][(i-600)//100]=2
                                else:
                                    inmatrix6[(j-300)//100][(i-600)//100]=1 
                                

                    for i in range (600,900,100):
                        for j in range (600,900,100):
                            if (today_dot[0]==i+50 and today_dot[1]==j+50):
                                
                                if today_dot[2]%2==0:
                                    inmatrix9[(j-600)//100][(i-600)//100]=2
                                else:
                                    inmatrix9[(j-600)//100][(i-600)//100]=1 
                                                                   
                    



                    # проверка выйгрыша где-либо
                    #############################################################################
                    #if win1==True:
                        if (inmatrix1[0][0]==inmatrix1[0][1] and inmatrix1[0][0]==inmatrix1[0][2]):
                            Win1=True 
                            mas1=((0,0)) 
                                
                        if (inmatrix1[1][0]==inmatrix1[1][1] and inmatrix1[1][0]==inmatrix1[1][2]):
                            Win1=True 
                            mas1=((0,0)) 
                                
                        if (inmatrix1[2][0]==inmatrix1[2][1] and inmatrix1[2][0]==inmatrix1[2][2]):
                            Win1=True 
                            mas1=((0,0))
                        
                        if (inmatrix1[0][0]==inmatrix1[1][0] and inmatrix1[0][0]==inmatrix1[2][0]):
                            Win1=True 
                            mas1=((0,0))
                        
                        if (inmatrix1[0][1]==inmatrix1[1][1] and inmatrix1[0][1]==inmatrix1[2][1]):
                            Win1=True 
                            mas1=((0,0))
                        
                        if (inmatrix1[0][2]==inmatrix1[1][2] and inmatrix1[0][2]==inmatrix1[2][2]):
                            Win1=True 
                            mas1=((0,0))
                        
                        if (inmatrix1[0][0]==inmatrix1[1][1] and inmatrix1[0][0]==inmatrix1[2][2]):
                            Win1=True 
                            mas1=((0,0))
                        
                        if (inmatrix1[0][2]==inmatrix1[1][1] and inmatrix1[0][2]==inmatrix1[2][0]):
                            Win1=True 
                            mas1=((0,0))
                    #############################################################################
                    #if win2==True:
                        if (inmatrix2[0][0]==inmatrix2[0][1] and inmatrix2[0][0]==inmatrix2[0][2]):
                            Win2=True 
                            mas2=((300,0))   
                                
                        if (inmatrix2[1][0]==inmatrix2[1][1] and inmatrix2[1][0]==inmatrix2[1][2]):
                            Win2=True
                            mas2=((300,0)) 
                            
                        if (inmatrix2[2][0]==inmatrix2[2][1] and inmatrix2[2][0]==inmatrix2[2][2]):
                            Win2=True
                            mas2=((300,0)) 
                        
                        if (inmatrix2[0][0]==inmatrix2[1][0] and inmatrix2[0][0]==inmatrix2[2][0]):
                            Win2=True
                            mas2=((300,0)) 
                        
                        if (inmatrix2[0][1]==inmatrix2[1][1] and inmatrix2[0][1]==inmatrix2[2][1]):
                            Win2=True
                            mas2=((300,0)) 
                        
                        if (inmatrix2[0][2]==inmatrix2[1][2] and inmatrix2[0][2]==inmatrix2[2][2]):
                            Win2=True
                            mas2=((300,0)) 
                        
                        if (inmatrix2[0][0]==inmatrix2[1][1] and inmatrix2[0][0]==inmatrix2[2][2]):
                            Win2=True
                            mas2=((300,0)) 
                        
                        if (inmatrix2[0][2]==inmatrix2[1][1] and inmatrix2[0][2]==inmatrix2[2][0]):
                            Win2=True
                            mas2=((300,0)) 
                    #############################################################################
                    #if win3==True:
                        if (inmatrix3[0][0]==inmatrix3[0][1] and inmatrix3[0][0]==inmatrix3[0][2]):
                            Win3=True
                            mas3=((600,0))
                                
                        if (inmatrix3[1][0]==inmatrix3[1][1] and inmatrix3[1][0]==inmatrix3[1][2]):
                            Win3=True
                            mas3=((600,0)) 
                                
                        if (inmatrix3[2][0]==inmatrix3[2][1] and inmatrix3[2][0]==inmatrix3[2][2]):
                            Win3=True
                            mas3=((600,0))
                        
                        if (inmatrix3[0][0]==inmatrix3[1][0] and inmatrix3[0][0]==inmatrix3[2][0]):
                            Win3=True
                            mas3=((600,0))
                        
                        if (inmatrix3[0][1]==inmatrix3[1][1] and inmatrix3[0][1]==inmatrix3[2][1]):
                            Win3=True
                            mas3=((600,0))
                        
                        if (inmatrix3[0][2]==inmatrix3[1][2] and inmatrix3[0][2]==inmatrix3[2][2]):
                            Win3=True
                            mas3=((600,0))
                        
                        if (inmatrix3[0][0]==inmatrix3[1][1] and inmatrix3[0][0]==inmatrix3[2][2]):
                            Win3=True
                            mas3=((600,0))
                        
                        if (inmatrix3[0][2]==inmatrix3[1][1] and inmatrix3[0][2]==inmatrix3[2][0]):
                            Win3=True
                            mas3=((600,0))
                    #############################################################################
                    #if win4==True:
                        if (inmatrix4[0][0]==inmatrix4[0][1] and inmatrix4[0][0]==inmatrix4[0][2]):
                            Win4=True
                            mas4=((0,300))
                        
                        if (inmatrix4[1][0]==inmatrix4[1][1] and inmatrix4[1][0]==inmatrix4[1][2]):
                            Win4=True
                            mas4=((0,300))
                                
                        if (inmatrix4[2][0]==inmatrix4[2][1] and inmatrix4[2][0]==inmatrix4[2][2]):
                            Win4=True
                            mas4=((0,300))
                        
                        if (inmatrix4[0][0]==inmatrix4[1][0] and inmatrix4[0][0]==inmatrix4[2][0]):
                            Win4=True
                            mas4=((0,300))
                        
                        if (inmatrix4[0][1]==inmatrix4[1][1] and inmatrix4[0][1]==inmatrix4[2][1]):
                            Win4=True
                            mas4=((0,300))
                        
                        if (inmatrix4[0][2]==inmatrix4[1][2] and inmatrix4[0][2]==inmatrix4[2][2]):
                            Win4=True
                            mas4=((0,300))
                        
                        if (inmatrix4[0][0]==inmatrix4[1][1] and inmatrix4[0][0]==inmatrix4[2][2]):
                            Win4=True
                            mas4=((0,300))
                        
                        if (inmatrix4[0][2]==inmatrix4[1][1] and inmatrix4[0][2]==inmatrix4[2][0]):
                            Win4=True
                            mas4=((0,300))
                    #############################################################################
                    #if win5==True:
                        if (inmatrix5[0][0]==inmatrix5[0][1] and inmatrix5[0][0]==inmatrix5[0][2]):
                            Win5=True
                            mas5=((300,300))  
                                
                        if (inmatrix5[1][0]==inmatrix5[1][1] and inmatrix5[1][0]==inmatrix5[1][2]):
                            Win5=True
                            mas5=((300,300))   
                                
                        if (inmatrix5[2][0]==inmatrix5[2][1] and inmatrix5[2][0]==inmatrix5[2][2]):
                            Win5=True
                            mas5=((300,300))  
                        
                        if (inmatrix5[0][0]==inmatrix5[1][0] and inmatrix5[0][0]==inmatrix5[2][0]):
                            Win5=True
                            mas5=((300,300))  
                        
                        if (inmatrix5[0][1]==inmatrix5[1][1] and inmatrix5[0][1]==inmatrix5[2][1]):
                            Win5=True
                            mas5=((300,300))  
                        
                        if (inmatrix5[0][2]==inmatrix5[1][2] and inmatrix5[0][2]==inmatrix5[2][2]):
                            Win5=True
                            mas5=((300,300))  
                        
                        if (inmatrix5[0][0]==inmatrix5[1][1] and inmatrix5[0][0]==inmatrix5[2][2]):
                            Win5=True
                            mas5=((300,300))  
                        
                        if (inmatrix5[0][2]==inmatrix5[1][1] and inmatrix5[0][2]==inmatrix5[2][0]):
                            Win5=True
                            mas5=((300,300))  
                    #############################################################################
                    #if win6==True:
                        if (inmatrix6[0][0]==inmatrix6[0][1] and inmatrix6[0][0]==inmatrix6[0][2]):
                            Win6=True
                            mas6=((600,300))   
                                
                        if (inmatrix6[1][0]==inmatrix6[1][1] and inmatrix6[1][0]==inmatrix6[1][2]):
                            Win6=True
                            mas6=((600,300))  
                                
                        if (inmatrix6[2][0]==inmatrix6[2][1] and inmatrix6[2][0]==inmatrix6[2][2]):
                            Win6=True
                            mas6=((600,300)) 
                        
                        if (inmatrix6[0][0]==inmatrix6[1][0] and inmatrix6[0][0]==inmatrix6[2][0]):
                            Win6=True
                            mas6=((600,300)) 
                        
                        if (inmatrix6[0][1]==inmatrix6[1][1] and inmatrix6[0][1]==inmatrix6[2][1]):
                            Win6=True
                            mas6=((600,300)) 
                    
                        if (inmatrix6[0][2]==inmatrix6[1][2] and inmatrix6[0][2]==inmatrix6[2][2]):
                            Win6=True
                            mas6=((600,300)) 
                        
                        if (inmatrix6[0][0]==inmatrix6[1][1] and inmatrix6[0][0]==inmatrix6[2][2]):
                            Win6=True
                            mas6=((600,300)) 
                        
                        if (inmatrix6[0][2]==inmatrix6[1][1] and inmatrix6[0][2]==inmatrix6[2][0]):
                            Win6=True
                            mas6=((600,300)) 
                    #############################################################################
                    #if win7==True:
                        if (inmatrix7[0][0]==inmatrix7[0][1] and inmatrix7[0][0]==inmatrix7[0][2]):
                            Win7=True  
                            mas7=((0,600))
                                
                        if (inmatrix7[1][0]==inmatrix7[1][1] and inmatrix7[1][0]==inmatrix7[1][2]):
                            Win7=True  
                            mas7=((0,600)) 
                                
                        if (inmatrix7[2][0]==inmatrix7[2][1] and inmatrix7[2][0]==inmatrix7[2][2]):
                            Win7=True  
                            mas7=((0,600))
                        
                        if (inmatrix7[0][0]==inmatrix7[1][0] and inmatrix7[0][0]==inmatrix7[2][0]):
                            Win7=True  
                            mas7=((0,600))
                        
                        if (inmatrix7[0][1]==inmatrix7[1][1] and inmatrix7[0][1]==inmatrix7[2][1]):
                            Win7=True  
                            mas7=((0,600))
                        
                        if (inmatrix7[0][2]==inmatrix7[1][2] and inmatrix7[0][2]==inmatrix7[2][2]):
                            Win7=True  
                            mas7=((0,600))
                        
                        if (inmatrix7[0][0]==inmatrix7[1][1] and inmatrix7[0][0]==inmatrix7[2][2]):
                            Win7=True  
                            mas7=((0,600))
                        
                        if (inmatrix7[0][2]==inmatrix7[1][1] and inmatrix7[0][2]==inmatrix7[2][0]):
                            Win7=True  
                            mas7=((0,600))
                    #############################################################################
                    #if win8==True:
                        if (inmatrix8[0][0]==inmatrix8[0][1] and inmatrix8[0][0]==inmatrix8[0][2]):
                            Win8=True
                            mas8=((300,600))   
                                
                        if (inmatrix8[1][0]==inmatrix8[1][1] and inmatrix8[1][0]==inmatrix8[1][2]):
                            Win8=True
                            mas8=((300,600))  
                                
                        if (inmatrix8[2][0]==inmatrix8[2][1] and inmatrix8[2][0]==inmatrix8[2][2]):
                            Win8=True
                            mas8=((300,600)) 
                        
                        if (inmatrix8[0][0]==inmatrix8[1][0] and inmatrix8[0][0]==inmatrix8[2][0]):
                            Win8=True
                            mas8=((300,600)) 
                        
                        if (inmatrix8[0][1]==inmatrix8[1][1] and inmatrix8[0][1]==inmatrix8[2][1]):
                            Win8=True
                            mas8=((300,600)) 
                        
                        if (inmatrix8[0][2]==inmatrix8[1][2] and inmatrix8[0][2]==inmatrix8[2][2]):
                            Win8=True
                            mas8=((300,600)) 
                        
                        if (inmatrix8[0][0]==inmatrix8[1][1] and inmatrix8[0][0]==inmatrix8[2][2]):
                            Win8=True
                            mas8=((300,600)) 
                        
                        if (inmatrix8[0][2]==inmatrix8[1][1] and inmatrix8[0][2]==inmatrix8[2][0]):
                            Win8=True
                            mas8=((300,600)) 
                    #############################################################################
                    #if win9==True:
                        if (inmatrix9[0][0]==inmatrix9[0][1] and inmatrix9[0][0]==inmatrix9[0][2]):
                            Win9=True
                            mas9=((600,600)) 
                                
                        if (inmatrix9[1][0]==inmatrix9[1][1] and inmatrix9[1][0]==inmatrix9[1][2]):
                            Win9=True
                            mas9=((600,600))
                                
                        if (inmatrix9[2][0]==inmatrix9[2][1] and inmatrix9[2][0]==inmatrix9[2][2]):
                            Win9=True
                            mas9=((600,600))
                        
                        if (inmatrix9[0][0]==inmatrix9[1][0] and inmatrix9[0][0]==inmatrix9[2][0]):
                            Win9=True
                            mas9=((600,600))
                        
                        if (inmatrix9[0][1]==inmatrix9[1][1] and inmatrix9[0][1]==inmatrix9[2][1]):
                            Win9=True
                            mas9=((600,600))
                        
                        if (inmatrix9[0][2]==inmatrix9[1][2] and inmatrix9[0][2]==inmatrix9[2][2]):
                            Win9=True
                            mas9=((600,600))
                        
                        if (inmatrix9[0][0]==inmatrix9[1][1] and inmatrix9[0][0]==inmatrix9[2][2]):
                            Win9=True
                            mas9=((600,600))
                        
                        if (inmatrix9[0][2]==inmatrix9[1][1] and inmatrix9[0][2]==inmatrix9[2][0]):
                            Win9=True
                            mas9=((600,600))
                    #############################################################################  

                    timer=False # вырубаем таймер, чтобы больше не обновлять текущий лист одной и той же точкой        
   
        ###################################################################################################################################################
        
        #шедевральный блок по рисовке зеленых квадратов
        #центр
        if grfl==True:
            if today_dot[0]%3==0 and today_dot[1]%3==0:
                pygame.draw.rect(dis, GreenYellow, [305,305,295,295])
                grx=300
                gry=300
            #центр верх    
            if today_dot[0]%3==0 and (today_dot[1]/50==1 or today_dot[1]/350==1 or today_dot[1]/650==1):
                pygame.draw.rect(dis, GreenYellow, [305,5,295,295]) 
                grx=300
                gry=0
            #центр низ          
            if today_dot[0]%3==0 and (today_dot[1]/250==1 or today_dot[1]/550==1 or today_dot[1]/850==1):
                pygame.draw.rect(dis, GreenYellow, [305,605,295,295]) 
                grx=300
                gry=600
            #лево верх    
            if (today_dot[0]/50==1 or today_dot[0]/350==1 or today_dot[0]/650==1) and (today_dot[1]/50==1 or today_dot[1]/350==1 or today_dot[1]/650==1):
                pygame.draw.rect(dis, GreenYellow, [5,5,295,295]) 
                grx=0
                gry=0 
            #лево центр    
            if (today_dot[0]/50==1 or today_dot[0]/350==1 or today_dot[0]/650==1) and (today_dot[1]/150==1 or today_dot[1]/450==1 or today_dot[1]/750==1):
                pygame.draw.rect(dis, GreenYellow, [5,305,295,295])
                grx=0
                gry=300
            #лево низ    
            if (today_dot[0]/50==1 or today_dot[0]/350==1 or today_dot[0]/650==1) and (today_dot[1]/250==1 or today_dot[1]/550==1 or today_dot[1]/850==1):
                pygame.draw.rect(dis, GreenYellow, [5,605,295,295])  
                grx=0
                gry=600         
            #право верх    
            if (today_dot[0]/250==1 or today_dot[0]/550==1 or today_dot[0]/850==1) and (today_dot[1]/50==1 or today_dot[1]/350==1 or today_dot[1]/650==1):
                pygame.draw.rect(dis, GreenYellow, [605,5,295,295])
                grx=600
                gry=0
            #право низ    
            if (today_dot[0]/250==1 or today_dot[0]/550==1 or today_dot[0]/850==1) and (today_dot[1]/150==1 or today_dot[1]/450==1 or today_dot[1]/750==1):
                pygame.draw.rect(dis, GreenYellow, [605,305,295,295])
                grx=600
                gry=300
            #право низ    
            if (today_dot[0]/250==1 or today_dot[0]/550==1 or today_dot[0]/850==1) and (today_dot[1]/250==1 or today_dot[1]/550==1 or today_dot[1]/850==1):
                pygame.draw.rect(dis, GreenYellow, [605,605,295,295]) 
                grx=600
                gry=600
        else:
            if ptoday_dot[0]%3==0 and ptoday_dot[1]%3==0:
                pygame.draw.rect(dis, GreenYellow, [305,305,295,295])
                grx=300
                gry=300
            #центр верх    
            if ptoday_dot[0]%3==0 and (ptoday_dot[1]/50==1 or ptoday_dot[1]/350==1 or ptoday_dot[1]/650==1):
                pygame.draw.rect(dis, GreenYellow, [305,5,295,295]) 
                grx=300
                gry=0
            #центр низ          
            if ptoday_dot[0]%3==0 and (ptoday_dot[1]/250==1 or ptoday_dot[1]/550==1 or ptoday_dot[1]/850==1):
                pygame.draw.rect(dis, GreenYellow, [305,605,295,295]) 
                grx=300
                gry=600
            #лево верх    
            if (ptoday_dot[0]/50==1 or ptoday_dot[0]/350==1 or ptoday_dot[0]/650==1) and (ptoday_dot[1]/50==1 or ptoday_dot[1]/350==1 or ptoday_dot[1]/650==1):
                pygame.draw.rect(dis, GreenYellow, [5,5,295,295]) 
                grx=0
                gry=0 
            #лево центр    
            if (ptoday_dot[0]/50==1 or ptoday_dot[0]/350==1 or ptoday_dot[0]/650==1) and (ptoday_dot[1]/150==1 or ptoday_dot[1]/450==1 or ptoday_dot[1]/750==1):
                pygame.draw.rect(dis, GreenYellow, [5,305,295,295])
                grx=0
                gry=300
            #лево низ    
            if (ptoday_dot[0]/50==1 or ptoday_dot[0]/350==1 or ptoday_dot[0]/650==1) and (ptoday_dot[1]/250==1 or ptoday_dot[1]/550==1 or ptoday_dot[1]/850==1):
                pygame.draw.rect(dis, GreenYellow, [5,605,295,295])  
                grx=0
                gry=600         
            #право верх    
            if (ptoday_dot[0]/250==1 or ptoday_dot[0]/550==1 or ptoday_dot[0]/850==1) and (ptoday_dot[1]/50==1 or ptoday_dot[1]/350==1 or ptoday_dot[1]/650==1):
                pygame.draw.rect(dis, GreenYellow, [605,5,295,295])
                grx=600
                gry=0
            #право низ    
            if (ptoday_dot[0]/250==1 or ptoday_dot[0]/550==1 or ptoday_dot[0]/850==1) and (ptoday_dot[1]/150==1 or ptoday_dot[1]/450==1 or ptoday_dot[1]/750==1):
                pygame.draw.rect(dis, GreenYellow, [605,305,295,295])
                grx=600
                gry=300
            #право низ    
            if (ptoday_dot[0]/250==1 or ptoday_dot[0]/550==1 or ptoday_dot[0]/850==1) and (ptoday_dot[1]/250==1 or ptoday_dot[1]/550==1 or ptoday_dot[1]/850==1):
                pygame.draw.rect(dis, GreenYellow, [605,605,295,295]) 
                grx=600
                gry=600        
            
        ###################################################################################################################################################
            
            # не менее шедевральный блок для закрашивания выйгранных клеток, win нужен для того, чтобы когда клетка закрашивается мы записывали в переменную 
            # текущую четность цвета, после чего мы вырубаем win, и цвет не будет больше менятся. Просто вырубить Win нельзя т.к иначе перестанется выводится
            # выйгранная клетка.
        
        
        if Win1==True:
                if win1==True:
                    x=today_dot[2]
                if x%2==0:
                    pygame.draw.rect(dis, green, [5,5,295,295])
                    if fl1==True:
                        today_mas=[]
                        today_mas.append(150)
                        today_mas.append(150)
                        today_mas.append(2)
                        fl1=False
                else:
                    pygame.draw.rect(dis, FireBrick, [5,5,295,295])
                    if fl1==True:
                        today_mas=[]
                        today_mas.append(150)
                        today_mas.append(150)
                        today_mas.append(1)
                        fl1=False
                win1=False 
        
        

        
        if Win2==True:
                if win2==True:
                    y=today_dot[2]
                if y%2==0:
                    pygame.draw.rect(dis, green, [305,5,295,295])
                    if fl2==True:
                        today_mas=[]
                        print(today_mas)
                        today_mas.append(450)
                        today_mas.append(150)
                        today_mas.append(2)
                        fl2=False
                else:
                    pygame.draw.rect(dis, FireBrick, [305,5,295,295])
                    if fl2==True:
                        today_mas=[]
                        print(today_mas)
                        today_mas.append(450)
                        today_mas.append(150)
                        today_mas.append(1)
                        fl2=False
                win2=False 

        
        
        
        if Win3==True:
                if win3==True:
                    u=today_dot[2]
                if u%2==0:
                    pygame.draw.rect(dis, green, [605,5,295,295])
                    if fl3==True:
                        today_mas=[]
                        today_mas.append(750)
                        today_mas.append(150)
                        today_mas.append(2)
                        fl3=False
                else:
                    pygame.draw.rect(dis, FireBrick, [605,5,295,295])
                    if fl3==True:
                        today_mas=[]
                        today_mas.append(750)
                        today_mas.append(150)
                        today_mas.append(1)
                        fl3=False
                win3=False 
        if Win4==True:
                if win4==True:
                    o=today_dot[2]
                if o%2==0:
                    pygame.draw.rect(dis, green, [5,305,295,295])
                    if fl4==True:
                        today_mas=[]
                        today_mas.append(150)
                        today_mas.append(450)
                        today_mas.append(2)
                        fl4=False
                else:
                    pygame.draw.rect(dis, FireBrick, [5,305,295,295])
                    if fl4==True:
                        today_mas=[]
                        today_mas.append(150)
                        today_mas.append(450)
                        today_mas.append(1)
                        fl4=False
                win4=False 
        if Win5==True:
                if win5==True:
                    p=today_dot[2]
                if p%2==0:
                    pygame.draw.rect(dis, green, [305,305,295,295])
                    if fl5==True:
                        today_mas=[]
                        today_mas.append(450)
                        today_mas.append(450)
                        today_mas.append(2)
                        fl5=False
                else:
                    pygame.draw.rect(dis, FireBrick, [305,305,295,295])
                    if fl5==True:
                        today_mas=[]
                        today_mas.append(450)
                        today_mas.append(450)
                        today_mas.append(1)
                        fl5=False
                win5=False 
        if Win6==True:
                if win6==True:
                    a=today_dot[2]
                if a%2==0:
                    pygame.draw.rect(dis, green, [605,305,295,295])
                    if fl6==True:
                        today_mas=[]
                        today_mas.append(750)
                        today_mas.append(450)
                        today_mas.append(2)
                        fl6=False
                else:
                    pygame.draw.rect(dis, FireBrick, [605,305,295,295])
                    if fl6==True:
                        today_mas=[]
                        today_mas.append(750)
                        today_mas.append(450)
                        today_mas.append(1)
                        fl6=False
                win6=False 
        if Win7==True:
                if win7==True:
                    s=today_dot[2]
                if s%2==0:
                    pygame.draw.rect(dis, green, [5,605,295,295])
                    if fl7==True:
                        today_mas=[]
                        today_mas.append(150)
                        today_mas.append(750)
                        today_mas.append(2)
                        fl7=False
                else:
                    pygame.draw.rect(dis, FireBrick, [5,605,295,295])
                    if fl7==True:
                        today_mas=[]
                        today_mas.append(150)
                        today_mas.append(750)
                        today_mas.append(1)
                        fl7=False
                win7=False

        if Win8==True:
                if win8==True:
                    d=today_dot[2]
                if d%2==0:
                    pygame.draw.rect(dis, green, [305,605,295,295])
                    if fl8==True:
                        today_mas=[]
                        today_mas.append(450)
                        today_mas.append(750)
                        today_mas.append(2)
                        fl8=False
                else:
                    pygame.draw.rect(dis, FireBrick, [305,605,295,295])
                    if fl8==True:
                        today_mas=[]
                        today_mas.append(450)
                        today_mas.append(750)
                        today_mas.append(1)
                        fl8=False
                win8=False 
        if Win9==True:
                if win9==True:
                    f=today_dot[2]
                if f%2==0:
                    pygame.draw.rect(dis, green, [605,605,295,295])
                    if fl9==True:
                        today_mas=[]
                        today_mas.append(750)
                        today_mas.append(750)
                        today_mas.append(2)
                        fl9=False
                else:
                    pygame.draw.rect(dis, FireBrick, [605,605,295,295])
                    if fl9==True:
                        today_mas=[]
                        today_mas.append(750)
                        today_mas.append(750)
                        today_mas.append(1)
                        fl9=False
                win9=False
       


        for i in range (0,900,300):
                        for j in range (0,900,300):
                            if (today_mas[0]==i+150 and today_mas[1]==j+150):
                                print(i,j)
                                if today_mas[2]%2==0:
                                    inmatrix[j//300][i//300]=2
                                else:
                                    inmatrix[j//300][i//300]=1  


        # блок ифов определяющих победу в большом поле
        if (inmatrix[0][0]==inmatrix[0][1] and inmatrix[0][0]==inmatrix[0][2]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
        if (inmatrix[1][0]==inmatrix[1][1] and inmatrix[1][0]==inmatrix[1][2]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
        if (inmatrix[2][0]==inmatrix[2][1] and inmatrix[2][0]==inmatrix[2][2]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
        if (inmatrix[0][0]==inmatrix[1][0] and inmatrix[0][0]==inmatrix[2][0]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
        if (inmatrix[0][1]==inmatrix[1][1] and inmatrix[0][1]==inmatrix[2][1]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
        if (inmatrix[0][2]==inmatrix[1][2] and inmatrix[0][2]==inmatrix[2][2]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
        if (inmatrix[0][0]==inmatrix[1][1] and inmatrix[0][0]==inmatrix[2][2]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
        if (inmatrix[0][2]==inmatrix[1][1] and inmatrix[0][2]==inmatrix[2][0]):
            if today_mas[2]%2==1:
                game_close=True
                gr=False
            else:
                game_close=True
                gr=True
                                   
        ###################################################################################################################################################
        
        # рисовка поля со всеми точками
        draw_dot(size,dot_list,cordsi,cords)
        mapa()                  
        pygame.display.update() 
        dis.fill(white)
        # FPS всей игры
        clock.tick(5)  

        ###########################################################################################################################################################

# ну, это были все функции, вот сама программа
gameloop()       