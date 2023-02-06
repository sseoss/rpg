import random
import time
class Player:
    def __init__(self, name , hp , damage, class_player , race_player):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.class_player = class_player
        self.race_player = race_player
        self.level = 1
        self.xp = 0
    @staticmethod
    def lvlup():
        player.xp = 0
        player.hp += 100 * player.level
        player.damage += 100 * player.level
        player.level += 1
        time.sleep(1)
        print(f'Ваш уровень повышен до {player.level}')
        return player.level
    def create_medic():
        medic = {
            100: "small medic",
            200: "big medic",
        }
        llllllllllllll = random.choice(list(medic.keys()))
        player.hp += llllllllllllll
        return medic[llllllllllllll]

    def create_weapon():
        weapon_list = ['sword', 'pistol' , 'bow' , 'laptop' , 'mouse' , 'key' , 'overclocking']
        rare_weapons = {
            100: 'rare',
            200: 'mythical',
            300: 'arcana',
            400:'legendary',
        }
        pppppppppppppppppp = weapon_list[random.randint(0,len(weapon_list)-1)]
        kkkkkkkkkkkk = random.choice(list(rare_weapons.keys()))
        if pppppppppppppppppp  == weapon_list[0]:
            player.damage += 1.2*kkkkkkkkkkkk
        elif pppppppppppppppppp  == weapon_list[1]:
            player.damage += 1.3*kkkkkkkkkkkk
        elif pppppppppppppppppp  == weapon_list[2]:
            player.damage += 1.4*kkkkkkkkkkkk
        elif pppppppppppppppppp  == weapon_list[3]:
            player.damage += 1.5*kkkkkkkkkkkk
        elif pppppppppppppppppp  == weapon_list[4]:
            player.damage += 1.6*kkkkkkkkkkkk
        elif pppppppppppppppppp  == weapon_list[5]:
            player.damage += 1.7*kkkkkkkkkkkk
        elif pppppppppppppppppp  == weapon_list[6]:
            player.damage += 1.8*kkkkkkkkkkkk
        return pppppppppppppppppp, rare_weapons[kkkkkkkkkkkk]
    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(f'{victim.name} повержен.+25 опыта!')
            time.sleep(0.5)
            self.xp += 25
            print(f'ВАШ ОПЫТ ТЕПЕРЬ {self.xp}')
            infinity_xp = 1 + self.level * 50
            if self.xp >= infinity_xp:
                Player.lvlup()
            jjjjjjjjjjjjj = random.choice(list(choice_list))
            if jjjjjjjjjjjjj == 'weapon':
                weapon = Player.create_weapon()
                print(weapon)
                print(f'ВАМ ВЫПАЛО ОРУЖИЕ!!!!{weapon[0]} , {weapon[1]}')
                print(f'ВАШ УРОН ТЕПЕРЬ {self.damage}')

                time.sleep(1)

            elif  jjjjjjjjjjjjj == "heels":
                heal = Player.create_medic()
                print(f'ВАМ ВЫПАЛА ХИЛКА {heal}')
                print(f'ВАШЕ ЗДОРОВЬЕ ТЕПЕРЬ {self.hp}')
            else:
                print('ошибка')


            return False
        else:
            print(f'{victim.name} осталось {victim.hp} здоровья ')
            return True
def createHero(name,  races_player , class_player):
    name = name
    hp = 0
    damage = 0
    if races_player == races_list[0]:
        hp += 500
        damage += 500
    elif races_player == races_list[1]:
        hp += 250
        damage += 300
    else:
        print('Извините, я не знаю такой расы')
    if class_player == class_list[0]:
        hp += 600
        damage += 250
    elif class_player == class_list[1]:
        hp += 500
        damage += 300
    else:
        print('Извините, я не знаю такой класс!')
    return Player(name,hp  , damage , class_player,  races_player)
class Enemy:
    def __init__(self, name , hp , damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print('ВЫ ПРОИГРАЛИ!')
            quit()
        else:
            print(f'{self.name} ударил вас и снес вам {self.damage} ')
            print(f'у вас осталось столько здоровья: {victim.hp} ')


enemy_names = ['vampir' , 'ogr' , 'dark seer' , 'lyashnik' , 'skelet' , 'clockwerk']
choice_list = ['weapon','heels']

def createEnemy():
    enemy_namerererer = random.choice(enemy_names)
    enemy_hp = random.randint(200,800) + player.level * 100
    enemy_damage = random.randint(100,300) + player.level * 100
    return Enemy(enemy_namerererer, enemy_hp,enemy_damage)
def fight_choice():
    ataka_vibor = int(input('Атаковать или бежать?(1,2)'))
    if ataka_vibor == 1:
        print('Вы начали атаку противника')
        ataka2 = player.attack(enemy)
        if ataka2:
            time.sleep(1)
            enemy.attack(player)
            fight_choice()
    elif ataka_vibor == 2:
        print('Вы убегаете от противника')
        ollllll = random.randint(0,1)
        if ollllll == 0:
            print('Вам не удалось сбежать ')
            enemy.attack(player)
            fight_choice()

        elif ollllll == 1:
            print('Ваш игрок успешно сбежал')
    else:
        print('Ошибка')
        fight_choice()










enemy_person = []
person = []
class_list = ['archer' , 'sword']
races_list = ['elf' , 'gnom']
print('Hi, input your name pls ')
person.append(input())
print(f'Choose your race')
for i in races_list:
    print(f'{i}', end=' ')
person.append(input().lower())
print(f'Choose your class')
for a in class_list:
    print(f'{a}', end=" ")
person.append(input().lower())
player = createHero(person[0] , person[1], person[2])
person.clear()
print(f' {player.name} , {player.hp} ,{player.damage}, {player.race_player}, {player.class_player}')
print('Начинаем важный поход в подземелье')
while True:
    event = random.randint(0,1)
    if event == 0:
        print('ВАМ НИКТО НЕ ВСТРЕТИЛСЯ, ИДЁМ ДАЛЬШЕ!')
        time.sleep(1)

    elif event == 1:
        print('ВАМ КТО ТО ВСТРЕТИЛСЯ, НЕ ИДЁМ ДАЛЬШЕ!')
        enemy = createEnemy()
        print(enemy.name , enemy.hp , enemy.damage)
        fight_choice()

    else:
        print('Ошибка программы, пока ')
        quit()
