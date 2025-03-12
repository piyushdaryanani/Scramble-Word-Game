from django.shortcuts import render, redirect
import random
from .models import GameResult

EASY_WORDS = [
    'CAT', 'DOG', 'SUN', 'HAT', 'CAR', 'BEE', 'COW', 'PIG', 'EGG', 'CUP',
    'BOX', 'BUS', 'TOY', 'BED', 'BAT', 'FOX', 'OWL', 'ANT', 'MUD', 'SKY',
    'PEN', 'KEY', 'MAP', 'ZIP', 'RUG', 'ROCK', 'TREE', 'BIRD', 'FISH', 'BOAT',
    'DOOR', 'BALL', 'STAR', 'MOON', 'RAIN', 'SNOW', 'LEAF', 'WOLF', 'JUMP',
    'WALK', 'PLAY', 'STOP', 'OPEN', 'DESK', 'SHOE', 'COAT', 'MILK', 'SOUP',
    'FOOD', 'LOVE'
]

EASY_WORD_DESCRIPTIONS = {
    'CAT': 'A small, furry pet that purrs and loves to play.',
    'DOG': 'A friendly pet that loves to run and fetch.',
    'SUN': 'The bright star that lights up our day.',
    'HAT': 'A fun accessory you wear on your head.',
    'CAR': 'A small vehicle that takes you places.',
    'BEE': 'A busy insect that makes honey and buzzes among flowers.',
    'COW': 'A gentle farm animal that gives milk.',
    'PIG': 'A cute animal that loves to roll in the mud.',
    'EGG': 'A small, oval food that comes from chickens.',
    'CUP': 'A small container used for drinking.',
    'BOX': 'A container that holds your treasures or toys.',
    'BUS': 'A large vehicle that carries many people.',
    'TOY': 'A fun item that you play with.',
    'BED': 'A cozy place where you sleep and dream.',
    'BAT': 'A small animal that flies at night.',
    'FOX': 'A clever animal with a bushy tail.',
    'OWL': 'A wise bird that hoots at night.',
    'ANT': 'A tiny insect that works hard in a colony.',
    'MUD': 'Wet, soft soil that is fun to play in.',
    'SKY': 'The blue space above us filled with clouds.',
    'PEN': 'A tool used for writing your ideas.',
    'KEY': 'A small object that opens locks.',
    'MAP': 'A drawing that shows directions and places.',
    'ZIP': 'A fast move or a fastener on clothing.',
    'RUG': 'A soft piece of fabric placed on the floor.',
    'ROCK': 'A small, hard piece of earth you can find outside.',
    'TREE': 'A tall plant with branches and leaves.',
    'BIRD': 'A feathered creature that sings and flies.',
    'FISH': 'A water creature that swims gracefully.',
    'BOAT': 'A small vessel that sails on water.',
    'DOOR': 'An entrance that opens and closes.',
    'BALL': 'A round object used in games and sports.',
    'STAR': 'A tiny light that twinkles in the night sky.',
    'MOON': 'A round object that lights up the night.',
    'RAIN': 'Drops of water falling from the sky.',
    'SNOW': 'Fluffy white flakes that fall during winter.',
    'LEAF': 'A green, flat part of a plant.',
    'WOLF': 'A wild animal known for its keen senses.',
    'JUMP': 'To leap off the ground using your legs.',
    'WALK': 'To move on foot at a steady pace.',
    'PLAY': 'To have fun with toys or games.',
    'STOP': 'To cease moving or doing something.',
    'OPEN': 'To make something not closed.',
    'DESK': 'A piece of furniture where you can study or draw.',
    'SHOE': 'Footwear that protects your feet.',
    'COAT': 'A warm garment worn in cold weather.',
    'MILK': 'A healthy drink that comes from cows.',
    'SOUP': 'A warm, tasty liquid food.',
    'FOOD': 'Something you eat to give you energy and strength.',
    'LOVE': 'A warm feeling of care and happiness.'
}

MEDIUM_WORDS = [
    'GAME', 'CODE', 'CLUB', 'HIKE', 'RACE', 'ZOOM', 'CHAT', 'SONG', 'TUNE',
    'BARK', 'GROW', 'JUMP', 'TIME', 'WOLF', 'ROPE', 'FLAG', 'FORT', 'BITE',
    'SAIL', 'POND', 'FARM', 'ROAD', 'POST', 'WISH', 'RING', 'DUSK', 'DAWN',
    'WIND', 'BLUE', 'GOLD', 'IRON', 'FIRE', 'WOOD', 'MARS', 'ECHO', 'PEEL',
    'MOSS', 'BOWL', 'HUGS', 'COZY', 'MILD', 'SOFA', 'CART', 'SINK', 'DOVE',
    'PUFF', 'MICE', 'JAZZ', 'BEAD', 'NODE'
]

MEDIUM_WORD_DESCRIPTIONS = {
    'GAME': 'A fun activity you play for enjoyment.',
    'CODE': 'A set of letters or numbers used to send secret messages.',
    'CLUB': 'A small group or a place where friends meet to have fun.',
    'HIKE': 'A walk, usually in nature, for exercise and fun.',
    'RACE': 'A competition to see who can run or drive the fastest.',
    'ZOOM': 'To move quickly, like a speedy race car.',
    'CHAT': 'A friendly talk between people.',
    'SONG': 'A short piece of music with words that you sing.',
    'TUNE': 'A pleasant melody that you can hum or sing.',
    'BARK': 'The sound a dog makes.',
    'GROW': 'To get bigger or develop over time.',
    'JUMP': 'To leap off the ground using your legs.',
    'TIME': 'What clocks measure, like seconds, minutes, and hours.',
    'WOLF': 'A wild animal known for its keen senses.',
    'ROPE': 'A thick string used for tying or climbing.',
    'FLAG': 'A piece of cloth that represents a country or team.',
    'FORT': 'A small, playful structure you build or visit.',
    'BITE': 'To use your teeth to cut into food.',
    'SAIL': 'To move on water using a boat’s sail.',
    'POND': 'A small body of still water where ducks might swim.',
    'FARM': 'A place where crops grow and animals are raised.',
    'ROAD': 'A path where vehicles travel.',
    'POST': 'A piece of wood or metal set upright, or a message sent online.',
    'WISH': 'A hopeful desire or dream for something good.',
    'RING': 'A small circular band, like jewelry or a bell’s sound.',
    'DUSK': 'The time when the day slowly turns into night.',
    'DAWN': 'The early morning when the sun first appears.',
    'WIND': 'Moving air you can feel on your face.',
    'BLUE': 'A color that reminds you of the clear sky or the ocean.',
    'GOLD': 'A shiny, yellow metal often associated with treasure.',
    'IRON': 'A strong metal used to build many things.',
    'FIRE': 'Bright, warm energy that burns and gives light.',
    'WOOD': 'The hard material that comes from trees.',
    'MARS': 'The red planet that twinkles in our solar system.',
    'ECHO': 'A sound that bounces back to you.',
    'PEEL': 'The skin or outer covering of a fruit or vegetable.',
    'MOSS': 'A soft, green plant that grows on rocks and trees.',
    'BOWL': 'A round dish used for holding food like soup or cereal.',
    'HUGS': 'Warm squeezes shared between friends.',
    'COZY': 'Comfortable and warm, like a soft blanket.',
    'MILD': 'Soft or not too strong in flavor or temperature.',
    'SOFA': 'A comfy seat to sit and relax on.',
    'CART': 'A small vehicle used for carrying things.',
    'SINK': 'A basin in the kitchen or bathroom where you wash up.',
    'DOVE': 'A gentle bird known for its soft cooing.',
    'PUFF': 'A small, soft burst of air or a light, fluffy texture.',
    'MICE': 'Small, quick animals that scurry around.',
    'JAZZ': 'A lively style of music with fun rhythms.',
    'BEAD': 'A tiny, round piece used for making jewelry.',
    'NODE': 'A small point or unit, like a dot in a network.'
}

HARD_WORDS = [
    'APPLE', 'BRICK', 'PLANT', 'GRASS', 'BEACH', 'CLOUD', 'SPACE', 'MAGIC',
    'DANCE', 'SMILE', 'HEART', 'DREAM', 'LIGHT', 'MUSIC', 'CROWN', 'WATER',
    'SUGAR', 'SWEET', 'BERRY', 'GRAPE', 'FRUIT', 'PLATE', 'PASTA', 'CANDY',
    'ANGEL', 'NIGHT', 'PARTY', 'STORY', 'FROST', 'STORM', 'EARTH', 'GLOBE',
    'ROBOT', 'CHEER', 'CLOWN', 'PIANO', 'VIOLA', 'FLUTE', 'VIVID', 'ZEBRA',
    'QUILT', 'PUPPY', 'KITTY', 'FABLE', 'NOVEL', 'PRIZE', 'GUEST', 'CLASP',
    'LASER', 'VIDEO'
]

HARD_WORD_DESCRIPTIONS = {
    'APPLE': 'A juicy fruit that can be red, green, or yellow.',
    'BRICK': 'A small, hard block used to build houses and walls.',
    'PLANT': 'A living green thing that grows in soil.',
    'GRASS': 'Soft, green blades covering the ground.',
    'BEACH': 'A sandy place by the ocean where you can play.',
    'CLOUD': 'A fluffy white shape floating in the sky.',
    'SPACE': 'The vast area beyond our planet, full of stars.',
    'MAGIC': 'A special, mysterious power that seems to make things happen.',
    'DANCE': 'Moving your body to music.',
    'SMILE': 'A happy, curved expression on your face.',
    'HEART': 'A symbol of love and care.',
    'DREAM': 'A special wish or idea you imagine, especially at night.',
    'LIGHT': 'What makes things visible; the brightness from the sun or a lamp.',
    'MUSIC': 'Pleasant sounds and songs that make you feel happy.',
    'CROWN': 'A shiny hat worn by kings or queens.',
    'WATER': 'A clear, refreshing liquid you drink or play in.',
    'SUGAR': 'A sweet substance used to make treats taste better.',
    'SWEET': 'Something that tastes sugary and delightful.',
    'BERRY': 'A small, juicy fruit that can be red or blue.',
    'GRAPE': 'A small, round fruit that grows in bunches.',
    'FRUIT': 'Tasty foods that grow on trees or bushes.',
    'PLATE': 'A flat dish used for serving meals.',
    'PASTA': 'Noodle-like food that tastes great with sauce.',
    'CANDY': 'A colorful, sweet treat enjoyed by many.',
    'ANGEL': 'A kind, gentle being with wings.',
    'NIGHT': 'The dark time after the sun sets.',
    'PARTY': 'A fun gathering with friends, music, and games.',
    'STORY': 'A tale full of adventures and fun characters.',
    'FROST': 'Tiny ice crystals that form when it’s cold.',
    'STORM': 'A wild weather event with wind and rain.',
    'EARTH': 'Our home planet, full of life and color.',
    'GLOBE': 'A round model of the Earth you can spin.',
    'ROBOT': 'A friendly machine that can move and help out.',
    'CHEER': 'A loud, happy shout of support or excitement.',
    'CLOWN': 'A funny performer with bright clothes and a big smile.',
    'PIANO': 'A musical instrument with black and white keys.',
    'VIOLA': 'A string instrument that makes warm, rich sounds.',
    'FLUTE': 'A light wind instrument that you play by blowing.',
    'VIVID': 'Bright and full of life, with strong colors.',
    'ZEBRA': 'An animal with striking black and white stripes.',
    'QUILT': 'A warm, patchwork cover used on a bed.',
    'PUPPY': 'A young dog that is playful and adorable.',
    'KITTY': 'A small, sweet cat that loves to cuddle.',
    'FABLE': 'A short story that teaches a lesson.',
    'NOVEL': 'A longer story filled with adventures.',
    'PRIZE': 'A reward given for doing something well.',
    'GUEST': 'A visitor or friend who comes over.',
    'CLASP': 'A small device used to fasten things together.',
    'LASER': 'A focused beam of light often used in fun shows.',
    'VIDEO': 'A moving picture that tells a story on a screen.'
}


def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def home(request):
    return render(request, 'game/home.html')


def easy_game(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
        request.session['correct_count'] = 0
        request.session['wrong_count'] = 0

    if request.method == 'POST':
        correct_word = request.session.get('correct_word')
        user_guess = request.POST.get('guess', '').strip().upper()

        # Check if the answer is correct
        if user_guess == correct_word:
            request.session['correct_count'] += 1
            result = "Correct! Well done."
        else:
            request.session['wrong_count'] += 1
            result = f"Oops! The correct word was '{correct_word}'."

        request.session['attempts'] += 1

        if request.session['attempts'] >= 10:
            GameResult.objects.create(
                player_name="Anonymous",
                difficulty="Easy",
                correct_count=request.session['correct_count'],
                wrong_count=request.session['wrong_count'],
                total_attempts=request.session['attempts']
            )
            return render(request, 'game/easy_game_over.html', {
                'correct_count': request.session['correct_count'],
                'wrong_count': request.session['wrong_count']
            })

        return render(request, 'game/easy.html', {
            'result': result,
            'user_guess': user_guess,
            'correct_word': correct_word,
        })


    else:
        word = random.choice(EASY_WORDS)
        scrambled = scramble_word(word)
        description = EASY_WORD_DESCRIPTIONS.get(word)

        request.session['correct_word'] = word

        # Calculate attempts left
        attempts = request.session.get('attempts', 0)
        attempts_left = 10 - attempts

        return render(request, 'game/game.html', {
            'scrambled': scrambled,
            'description': description,
            'attempts_left': attempts_left,
        })

def medium_game(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
        request.session['correct_count'] = 0
        request.session['wrong_count'] = 0

    if request.method == 'POST':
        correct_word = request.session.get('correct_word')
        user_guess = request.POST.get('guess', '').strip().upper()

        if user_guess == correct_word:
            request.session['correct_count'] += 1
            result = "Correct! Well done."
        else:
            request.session['wrong_count'] += 1
            result = f"Oops! The correct word was '{correct_word}'."

        request.session['attempts'] += 1

        if request.session['attempts'] >= 10:
            GameResult.objects.create(
                player_name="Anonymous",  # default name
                difficulty="Medium",
                correct_count=request.session['correct_count'],
                wrong_count=request.session['wrong_count'],
                total_attempts=request.session['attempts']
            )
            return render(request, 'game/medium_game_over.html', {
                'correct_count': request.session['correct_count'],
                'wrong_count': request.session['wrong_count']
            })

        return render(request, 'game/medium.html', {
            'result': result,
            'user_guess': user_guess,
            'correct_word': correct_word,
        })

    else:
        word = random.choice(MEDIUM_WORDS)
        scrambled = scramble_word(word)
        description = MEDIUM_WORD_DESCRIPTIONS.get(word)

        request.session['correct_word'] = word

        # Calculate attempts left
        attempts = request.session.get('attempts', 0)
        attempts_left = 10 - attempts

        return render(request, 'game/game.html', {
            'scrambled': scrambled,
            'description': description,
            'attempts_left': attempts_left,
        })

def hard_game(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
        request.session['correct_count'] = 0
        request.session['wrong_count'] = 0

    if request.method == 'POST':
        correct_word = request.session.get('correct_word')
        user_guess = request.POST.get('guess', '').strip().upper()

        if user_guess == correct_word:
            request.session['correct_count'] += 1
            result = "Correct! Well done."
        else:
            request.session['wrong_count'] += 1
            result = f"Oops! The correct word was '{correct_word}'."

        request.session['attempts'] += 1

        if request.session['attempts'] >= 10:
            GameResult.objects.create(
                player_name="Anonymous",
                difficulty="Hard",
                correct_count=request.session['correct_count'],
                wrong_count=request.session['wrong_count'],
                total_attempts=request.session['attempts']
            )
            return render(request, 'game/hard_game_over.html', {
                'correct_count': request.session['correct_count'],
                'wrong_count': request.session['wrong_count']
            })

        return render(request, 'game/hard.html', {
            'result': result,
            'user_guess': user_guess,
            'correct_word': correct_word,
        })

    else:
        word = random.choice(HARD_WORDS)
        scrambled = scramble_word(word)
        description = HARD_WORD_DESCRIPTIONS.get(word)

        request.session['correct_word'] = word

        # Calculate attempts left
        attempts = request.session.get('attempts', 0)
        attempts_left = 10 - attempts

        return render(request, 'game/game.html', {
            'scrambled': scrambled,
            'description': description,
            'attempts_left': attempts_left,
        })

def options(request):
    return render(request, 'game/options.html')

def game_rules(request):
     return render(request, 'game/gamerules.html')

def select_difficulty(request):
    request.session.flush()
    return render(request, 'game/difficulty.html')

def exit(request):
    return render("Exit")

def restart_easy(request):
    request.session.flush()
    return redirect('easy_game')

# Restart Medium Game
def restart_medium(request):
    request.session.flush()
    return redirect('medium_game')

# Restart Hard Game
def restart_hard(request):
    request.session.flush()
    return redirect('hard_game')