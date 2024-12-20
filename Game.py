import pygame
from pygame.locals import *
import sys
import os
import json
import random
from resources import *

pygame.init()
pygame.display.set_caption('Гра в кості "Яхта"')
screen = pygame.display.set_mode((768, 960), pygame.NOFRAME)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
mainClock = pygame.time.Clock()
font = pygame.font.Font('Digivolve.otf', 42)
fontmedium = pygame.font.Font('Digivolve.otf', 28)
fontmain = pygame.font.Font('Digivolve.otf', 16)
gui_bg = pygame.image.load(os.path.join("assets", "gui_bg.png")).convert_alpha()
gui_invisible = pygame.image.load(os.path.join("assets", "gui_invisible.png")).convert_alpha()
gui_scroll = pygame.image.load(os.path.join("assets", "gui_scroll.png")).convert_alpha()
gui_dicebig = pygame.image.load(os.path.join("assets", "img_dicebig.png")).convert_alpha()
gui_rules = pygame.image.load(os.path.join("assets", "gui_rules.png")).convert_alpha()
gui_scoreboardleft = pygame.image.load(os.path.join("assets", "gui_scoreboardleft.png")).convert_alpha()
gui_scoreboardright = pygame.image.load(os.path.join("assets", "gui_scoreboardright.png")).convert_alpha()
gui_btnmenudisabled = pygame.image.load(os.path.join("assets", "gui_btnmenudisabled.png")).convert_alpha()
gui_btnmenu = pygame.image.load(os.path.join("assets", "gui_btnmenu.png")).convert_alpha()
gui_btnmenulight = pygame.image.load(os.path.join("assets", "gui_btnmenulight.png")).convert_alpha()
gui_btnno = pygame.image.load(os.path.join("assets", "gui_btnno.png")).convert_alpha()
gui_btnnolight = pygame.image.load(os.path.join("assets", "gui_btnnolight.png")).convert_alpha()
gui_btnyes = pygame.image.load(os.path.join("assets", "gui_btnyes.png")).convert_alpha()
gui_btnyeslight = pygame.image.load(os.path.join("assets", "gui_btnyeslight.png")).convert_alpha()
gui_btnminimize = pygame.image.load(os.path.join("assets", "gui_btnminimize.png")).convert_alpha()
gui_btnminimizelight = pygame.image.load(os.path.join("assets", "gui_btnminimizelight.png")).convert_alpha()
gui_btnplus = pygame.image.load(os.path.join("assets", "gui_btnplus.png")).convert_alpha()
gui_btnpluslight = pygame.image.load(os.path.join("assets", "gui_btnpluslight.png")).convert_alpha()
gui_btnminus = pygame.image.load(os.path.join("assets", "gui_btnminus.png")).convert_alpha()
gui_btnminuslight = pygame.image.load(os.path.join("assets", "gui_btnminuslight.png")).convert_alpha()
gui_btnarrowleft = pygame.image.load(os.path.join("assets", "gui_btnarrowleft.png")).convert_alpha()
gui_btnarrowleftlight = pygame.image.load(os.path.join("assets", "gui_btnarrowleftlight.png")).convert_alpha()
gui_btnreroll = pygame.image.load(os.path.join("assets", "gui_btnreroll.png")).convert_alpha()
gui_btnrerolllight = pygame.image.load(os.path.join("assets", "gui_btnrerolllight.png")).convert_alpha()
gui_btnrolldisabled = pygame.image.load(os.path.join("assets", "gui_btnrolldisabled.png")).convert_alpha()
gui_btnroll = pygame.image.load(os.path.join("assets", "gui_btnroll.png")).convert_alpha()
gui_btnrolllight = pygame.image.load(os.path.join("assets", "gui_btnrolllight.png")).convert_alpha()
dice_one = pygame.image.load(os.path.join("assets", "dice_one.png")).convert_alpha()
dice_two = pygame.image.load(os.path.join("assets", "dice_two.png")).convert_alpha()
dice_three = pygame.image.load(os.path.join("assets", "dice_three.png")).convert_alpha()
dice_four = pygame.image.load(os.path.join("assets", "dice_four.png")).convert_alpha()
dice_five = pygame.image.load(os.path.join("assets", "dice_five.png")).convert_alpha()
dice_six = pygame.image.load(os.path.join("assets", "dice_six.png")).convert_alpha()

def draw_text(text, font, color, surface, position):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(topleft=position)
    surface.blit(textobj, textrect)

def draw_centeredtext(text, font, color, surface, position):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=position)
    surface.blit(textobj, textrect)

def create_button(button, image, hoverimage, position, callback, enabled=True, btnidx=0, btnidy=0):
    button["image"] = image
    button["rect"] = image.get_rect(center=position)
    button["callback"] = callback
    button["enabled"] = enabled
    button["idx"] = btnidx
    button["idy"] = btnidy
    screen.blit(button["image"], button["rect"])
    if enabled == True:
        if button["rect"].collidepoint(pygame.mouse.get_pos()):
            button["image"] = hoverimage
            screen.blit(button["image"], button["rect"])
    elif enabled == False:
        button["image"] = gui_btnmenudisabled

def create_textbutton(button, image, hoverimage, text, font, position, callback, enabled=True):
    button["image"] = image
    button["rect"] = image.get_rect(center=position)
    button["callback"] = callback
    button["enabled"] = enabled
    screen.blit(button["image"], button["rect"])
    draw_centeredtext(text, font, (224, 224, 224), screen, position)
    if enabled == True:
        if button["rect"].collidepoint(pygame.mouse.get_pos()):
            button["image"] = hoverimage
            screen.blit(button["image"], button["rect"])
            draw_centeredtext(text, font, (255, 255, 160), screen, position)
    elif enabled == False:
        button["image"] = gui_btnmenudisabled
        draw_centeredtext(text, font, (160, 160, 160), screen, position)

def button_on_click(button, event):
    if button["enabled"] == True:
        if event.button == 1:
            if button["rect"].collidepoint(event.pos):
                button["callback"](button)

def save_data():
    with open('gamedata.json', 'w') as file:
        json.dump(data, file, indent=2)

def clear_data(toclear):
    toclear['canContinue'] = False
    toclear['playerTurn'] = 0
    toclear['turnCount'] = 0
    toclear['rolls'] = 3
    toclear['diceOne'] = 0
    toclear['diceTwo'] = 0
    toclear['diceThree'] = 0
    toclear['diceFour'] = 0
    toclear['diceFive'] = 0
    for i in range(4):
        for n in range(13):
            toclear['stats'][i][combs[n]] = -1

def btn_closegame(button):
    save_data()
    pygame.quit()
    sys.exit()

def btn_minimizegame(button):
    pygame.display.iconify()

def btn_back(button):
    save_data()
    main_menu()

def btn_continuegame(button):
    play()

def btn_newgame(button):
    newgame()

def btn_rules(button):
    rules()

def btn_minus(button):
    data['playerCount'] -= 1

def btn_plus(button):
    data['playerCount'] += 1

def btn_creategame(button):
    clear_data(data)
    data['canContinue'] = True
    save_data()
    play()

try:
    with open('gamedata.json') as file:
        data = json.load(file)
except:
    print('default gamedata created')

save_data()

click = False

def main_menu():
    while True:
        screen.fill((0,0,0))
        screen.blit(gui_bg, (0, 0))
        screen.blit(gui_scroll, (10, 10))
        screen.blit(gui_dicebig, (264, 160))

        draw_text('Головне меню', font, (109, 43, 28), screen, (130, 36))

        button_quit = {}
        button_minimize = {}
        create_button(button_quit, gui_btnno, gui_btnnolight, (742, 26), btn_closegame)
        create_button(button_minimize, gui_btnminimize, gui_btnminimizelight, (706, 26), btn_minimizegame)

        button_continue = {}
        button_newgame = {}
        button_rules = {}
        create_textbutton(button_continue, gui_btnmenudisabled, gui_btnmenulight, "Продовжити", fontmedium, (WIDTH/2, 522), btn_continuegame, enabled=False)
        create_textbutton(button_newgame, gui_btnmenu, gui_btnmenulight, "Нова гра", fontmedium, (WIDTH/2, 612), btn_newgame)
        create_textbutton(button_rules, gui_btnmenu, gui_btnmenulight, "Правила", fontmedium, (WIDTH/2, 702), btn_rules)

        if data['canContinue'] == True:
            button_continue["enabled"] = True
            button_continue["image"] = gui_btnmenu
            screen.blit(button_continue["image"], button_continue["rect"])
            draw_centeredtext("Продовжити", fontmedium, (224, 224, 224), screen, (WIDTH/2, 522))
            if button_continue["rect"].collidepoint(pygame.mouse.get_pos()):
                button_continue["image"] = gui_btnmenulight
                screen.blit(button_continue["image"], button_continue["rect"])
                draw_centeredtext('Продовжити', fontmedium, (255, 255, 160), screen, (WIDTH/2, 522))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                save_data()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                button_on_click(button_quit, event)
                button_on_click(button_minimize, event)
                button_on_click(button_continue, event)
                button_on_click(button_newgame, event)
                button_on_click(button_rules, event)

        pygame.display.update()
        mainClock.tick(60)

dices_image = [dice_one, dice_two, dice_three, dice_four, dice_five, dice_six]
dices = [{"value": data['diceOne'], "reroll": False}, {"value": data['diceTwo'], "reroll": False}, {"value": data['diceThree'], "reroll": False}, {"value": data['diceFour'], "reroll": False}, {"value": data['diceFive'], "reroll": False}]
current = [dices[0]['value'], dices[1]['value'], dices[2]['value'], dices[3]['value'], dices[4]['value']]

def get_dice_image(n):
    if dices[n]['value'] == 0:
        return gui_invisible
    else:
        for i in range(1, 7):
            if dices[n]['value'] == i:
                return dices_image[i-1]

def check_sum_of_single(selected):
    return sum([x for x in current if x == selected])

def number_repeat(minRepeats):
    unique = set(current)
    repeats = [x for x in unique if len([y for y in current if y == x]) >= minRepeats]
    return repeats[0] if repeats else 0

def check_of_a_kind(n):
    return number_repeat(n) * n

def check_ones():
    return check_sum_of_single(1)

def check_twos():
    return check_sum_of_single(2)

def check_threes():
    return check_sum_of_single(3)

def check_fours():
    return check_sum_of_single(4)

def check_fives():
    return check_sum_of_single(5)

def check_sixes():
    return check_sum_of_single(6)

def check_set():
    return check_of_a_kind(3)

def check_quad():
    return check_of_a_kind(4)

def check_full_house():
    zcur = sorted(current)
    if (zcur[0] == zcur[1]) and (zcur[1] == zcur[2]) and (zcur[3] == zcur[4]) and (zcur[2] != zcur[3]):
        return sum(zcur)
    elif (zcur[0] == zcur[1]) and (zcur[2] == zcur[3]) and (zcur[3] == zcur[4]) and (zcur[1] != zcur[2]):
        return sum(zcur)
    else:
        return 0

def check_small_straight():
    if all(x in current for x in range(1, 5)):
        return 25
    elif all(x in current for x in range(2, 6)):
        return 25
    elif all(x in current for x in range(3, 7)):
        return 25
    else:
        return 0

def check_large_straight():
    if all(x in current for x in range(1, 6)):
        return 30
    elif all(x in current for x in range(2, 7)):
        return 30
    else:
        return 0

def check_yahtzee():
    return 50 if len(set(current)) == 1 else 0

def check_any():
    return sum(current)

def check_combination():
    combpoints['Ones'] = check_ones()
    combpoints['Twos'] = check_twos()
    combpoints['Threes'] = check_threes()
    combpoints['Fours'] = check_fours()
    combpoints['Fives'] = check_fives()
    combpoints['Sixes'] = check_sixes()
    combpoints['Set'] = check_set()
    combpoints['Quad'] = check_quad()
    combpoints['FullHouse'] = check_full_house()
    combpoints['ShortStraight'] = check_small_straight()
    combpoints['LongStraight'] = check_large_straight()
    combpoints['Yahtzee'] = check_yahtzee()
    combpoints['Any'] = check_any()

def cbox_reroll(button):
    buttonid = button["idx"]
    if dices[buttonid]["reroll"] == False:
        dices[buttonid]["reroll"] = True
    elif dices[buttonid]["reroll"] == True:
        dices[buttonid]["reroll"] = False

def btn_roll(button):
    if data['rolls'] == 3:
        for i in range(5):
            current[i] = random.randrange(1, 7)
            dices[i]["value"] = current[i]
    else:
        for i in range(5):
            if dices[i]["reroll"] == True:
                current[i] = random.randrange(1, 7)
                dices[i]["value"] = current[i]
    data['rolls'] -= 1
    data['diceOne'] = dices[0]['value']
    data['diceTwo'] = dices[1]['value']
    data['diceThree'] = dices[2]['value']
    data['diceFour'] = dices[3]['value']
    data['diceFive'] = dices[4]['value']
    save_data()
    check_combination()

def btn_choose_comb(button):
    buttonidx = button["idx"]
    buttonidy = button["idy"]
    data['stats'][buttonidx][combs[buttonidy]] = combpoints[combs[buttonidy]]
    if data['playerTurn'] == (data['playerCount']-1):
        data['playerTurn'] = 0
    else:
        data['playerTurn'] += 1
    data['turnCount'] += 1
    data['rolls'] = 3
    data['diceOne'] = 0
    data['diceTwo'] = 0
    data['diceThree'] = 0
    data['diceFour'] = 0
    data['diceFive'] = 0
    for i in range(5):
        dices[i]["reroll"] = False
    save_data()

def play():
    running = True
    check_combination()
    while running:
        screen.fill((0,0,0))
        screen.blit(gui_bg, (0, 0))
        screen.blit(gui_scoreboardleft, (28, 182))

        button_back = {}
        button_quit = {}
        button_minimize = {}
        create_button(button_back, gui_btnarrowleft, gui_btnarrowleftlight, (646, 26), btn_back)
        create_button(button_quit, gui_btnno, gui_btnnolight, (742, 26), btn_closegame)
        create_button(button_minimize, gui_btnminimize, gui_btnminimizelight, (706, 26), btn_minimizegame)

        buttons_reroll = [{}, {}, {}, {}, {}]
        buttons_choose = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        result = [0, 0, 0, 0]

        for i in combinations:
            draw_centeredtext(i, fontmain, (224, 224, 224), screen, (28 + 80, 206 + (combinations.index(i) * 50)))

        for i in range(data['playerCount']):
            screen.blit(gui_scoreboardright, (188 + (i * 138), 182))
            draw_centeredtext('Гравець {0}'.format(i+1), fontmain, (224, 224, 224), screen, (188 + 69 + (i * 138), 206))
            for n in range(13):
                if data['stats'][i][combs[n]] >= 0:
                    draw_centeredtext(str(data['stats'][i][combs[n]]), fontmain, (224, 224, 224), screen, (188 + 69 + (i * 138), 256 + (n * 50)))
                    result[i] += data['stats'][i][combs[n]]
            draw_centeredtext(str(result[i]), fontmain, (224, 224, 224), screen, (188 + 69 + (i * 138), 906))

        for i in range(13):
            image = gui_btnyes
            enable = True
            if data['rolls'] == 3 or data['stats'][data['playerTurn']][combs[i]] >= 0:
                image = gui_invisible
                enable = False
            create_button(buttons_choose[i], image, gui_btnyeslight, (188 + 69 + (data['playerTurn'] * 138), 256 + (i * 50)), btn_choose_comb, enabled=enable, btnidx=data['playerTurn'], btnidy=i)

        for i in range(5):
            if data['rolls'] != 3:
                screen.blit(get_dice_image(i), (280 + (i * 72), 66))
            image = gui_btnreroll
            imagetrue = gui_btnrerolllight
            enable = True
            if data['rolls'] == 3:
                image = gui_invisible
                enable = False
            if dices[i]["reroll"] == False:
                create_button(buttons_reroll[i], image, gui_btnrerolllight, (312 + (i * 72), 154), cbox_reroll, enabled=enable, btnidx=i)
            if dices[i]["reroll"] == True:
                create_button(buttons_reroll[i], imagetrue, gui_btnrerolllight, (312 + (i * 72), 154), cbox_reroll, enabled=enable, btnidx=i)

        progress = ''
        size = fontmain
        if data['rolls'] == 3:
            current_turn = 'Кинути кості'
            progress = 'Гравець {0} кидае кості'.format(data['playerTurn']+1)
            size = fontmedium
        if data['rolls'] == 2:
            current_turn = 'Перекинути'
            progress = 'Гравець {0} може перекинути кості ще {1} рази'.format(data['playerTurn']+1, data['rolls'])
        if data['rolls'] == 1:
            current_turn = 'Перекинути'
            progress = 'Гравець {0} може перекинути кості ще {1} раз'.format(data['playerTurn']+1, data['rolls'])
        if data['rolls'] == 0:
            current_turn = 'Зробіть вибір'
            progress = 'Гравець {0} обирае комбінацію для заповнення'.format(data['playerTurn']+1)
        if data['turnCount'] == (data['playerCount'] * 13):
            current_turn = 'Гру закінчено'
            progress = 'Гру закінчено! Переміг гравець {0}'.format(result.index(max(result))+1)
            size = fontmedium

        draw_text(progress, size, (160, 160, 160), screen, (16, 16))

        button_roll = {}
        create_textbutton(button_roll, gui_btnroll, gui_btnrolllight, current_turn, fontmain, (146, 112), btn_roll)

        if data['rolls'] == 0 or data['turnCount'] == (data['playerCount'] * 13):
            button_roll["enabled"] = False
            button_roll["image"] = gui_btnrolldisabled
            screen.blit(button_roll["image"], button_roll["rect"])
            draw_centeredtext(current_turn, fontmain, (160, 160, 160), screen, (146, 112))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                button_on_click(button_back, event)
                button_on_click(button_quit, event)
                button_on_click(button_minimize, event)
                button_on_click(button_roll, event)
                for i in buttons_reroll:
                    button_on_click(i, event)
                for i in buttons_choose:
                    button_on_click(i, event)

        pygame.display.update()
        mainClock.tick(60)

def newgame():
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(gui_bg, (0, 0))
        screen.blit(gui_scroll, (10, 10))
        screen.blit(gui_dicebig, (264, 160))

        draw_text('Нова гра', font, (109, 43, 28), screen, (160, 36))
        draw_text('Кількість гравців (2-4):', fontmedium, (224, 224, 224), screen, (110, 500))
        draw_text(str(data['playerCount']), fontmedium, (224, 224, 224), screen, (590, 500))

        button_back = {}
        button_quit = {}
        button_minimize = {}
        create_button(button_back, gui_btnarrowleft, gui_btnarrowleftlight, (646, 26), btn_back)
        create_button(button_quit, gui_btnno, gui_btnnolight, (742, 26), btn_closegame)
        create_button(button_minimize, gui_btnminimize, gui_btnminimizelight, (706, 26), btn_minimizegame)

        button_minus = {}
        button_plus = {}
        button_creategame = {}
        create_button(button_minus, gui_btnminus, gui_btnminuslight, (558, 518), btn_minus, enabled=False)
        create_button(button_plus, gui_btnplus, gui_btnpluslight, (640, 518), btn_plus, enabled=False)
        create_textbutton(button_creategame, gui_btnmenu, gui_btnmenulight, "Створити гру", fontmedium, (WIDTH/2, 682), btn_creategame)

        if data['playerCount'] > 2:
            button_minus["enabled"] = True
            if button_minus["rect"].collidepoint(pygame.mouse.get_pos()):
                button_minus["image"] = gui_btnminuslight
                screen.blit(button_minus["image"], button_minus["rect"])
        if data['playerCount'] < 4:
            button_plus["enabled"] = True
            if button_plus["rect"].collidepoint(pygame.mouse.get_pos()):
                button_plus["image"] = gui_btnpluslight
                screen.blit(button_plus["image"], button_plus["rect"])

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                save_data()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                button_on_click(button_back, event)
                button_on_click(button_quit, event)
                button_on_click(button_minimize, event)
                button_on_click(button_minus, event)
                button_on_click(button_plus, event)
                button_on_click(button_creategame, event)

        pygame.display.update()
        mainClock.tick(60)

def rules():
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(gui_bg, (0, 0))
        screen.blit(gui_scroll, (10, 10))
        screen.blit(gui_rules, (0, 0))

        draw_text('Правила гри', font, (109, 43, 28), screen, (130, 36))

        button_back = {}
        button_quit = {}
        button_minimize = {}
        create_button(button_back, gui_btnarrowleft, gui_btnarrowleftlight, (646, 26), btn_back)
        create_button(button_quit, gui_btnno, gui_btnnolight, (742, 26), btn_closegame)
        create_button(button_minimize, gui_btnminimize, gui_btnminimizelight, (706, 26), btn_minimizegame)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                save_data()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                button_on_click(button_back, event)
                button_on_click(button_quit, event)
                button_on_click(button_minimize, event)

        pygame.display.update()
        mainClock.tick(60)

main_menu()