# -*- coding: utf-8 -*-
"""小学 96 个 Unit 的扩充题素材：首字母填空短文（4—5 空）+ 连词成句（1 句）。

短文按教材话题自写，空格答案均为本单元核心词或其变形；连词成句考查同一单元的
核心句型，答案给出完整句子，accept 覆盖常见标点与缩写写法。
"""

EXTRA = {

    # ==================================================== 三年级上册
    ("3上", 1): dict(
        p="Good ___1___! My ___2___ is Kitty. In the morning I say ___3___ to my teacher. "
          "In the afternoon I say “Good ___4___!” to my friends.",
        a=["morning", "name", "hello", "afternoon"],
        s=("afternoon / Good / , / Kitty / !", "Good afternoon, Kitty!",
           ["Good afternoon Kitty!"]),
    ),
    ("3上", 2): dict(
        p="“How are you?” “I am ___1___, thank you.” My friend is not ___2___ today, because he has a "
          "cold. “I hope you get ___3___ soon,” I say. After school we say ___4___ to each other.",
        a=["fine", "well", "well", "goodbye"],
        s=("you / are / How / ?", "How are you?", ["How are you"]),
    ),
    ("3上", 3): dict(
        p="“Are you Kitty?” “___1___, I am.” “Are you Peter?” “___2___, I am ___3___ Peter. I am Tom.” "
          "“Oh, sorry!” “That's all right. Nice to meet ___4___.”",
        a=["Yes", "No", "not", "you"],
        s=("you / Are / Kitty / ?", "Are you Kitty?", ["Are you Kitty"]),
    ),
    ("3上", 4): dict(
        p="I have three ___1___. Tom is ___2___ and strong. Lily is ___3___, but she runs fast. "
          "Ben is ___4___; he does not eat much.",
        a=["friends", "tall", "short", "thin"],
        s=("is / My / tall / father / .", "My father is tall.", ["My father is tall"]),
    ),
    ("3上", 5): dict(
        p="This is my ___1___. He is a doctor. My ___2___ is a teacher. I have a big ___3___ and a "
          "little ___4___. We love each other.",
        a=["father", "mother", "brother", "sister"],
        s=("my / is / This / sister / .", "This is my sister.", ["This is my sister"]),
    ),
    ("3上", 6): dict(
        p="Look at me. I have two big ___1___, so I can see well. I can hear with my ___2___. I smell "
          "flowers with my ___3___, and I eat with my ___4___.",
        a=["eyes", "ears", "nose", "mouth"],
        s=("have / I / two / eyes / .", "I have two eyes.", ["I have two eyes"]),
    ),
    ("3上", 7): dict(
        p="This is my classroom. There is a big ___1___ on the wall. My ___2___ is near the window. "
          "I sit on a ___3___. Please open the ___4___; it is hot today.",
        a=["blackboard", "desk", "chair", "window"],
        s=("a / There / is / blackboard / .", "There is a blackboard.", ["There is a blackboard"]),
    ),
    ("3上", 8): dict(
        p="Let's go to the fruit shop. I would like an ___1___ and a ___2___. My sister wants an "
          "___3___ and a ___4___. Fruit is good for us.",
        a=["apple", "banana", "orange", "pear"],
        s=("like / I / an / would / apple / .", "I would like an apple.",
           ["I would like an apple"]),
    ),
    ("3上", 9): dict(
        p="This is my room. My ___1___ is big and soft. There is a ___2___ on the desk. My ball is "
          "___3___ the bed, and my book is ___4___ the desk.",
        a=["bed", "box", "under", "on"],
        s=("is / The / on / ball / bed / the / .", "The ball is on the bed.",
           ["The ball is on the bed"]),
    ),
    ("3上", 10): dict(
        p="I can count from one to ___1___. There are ten boys and ___2___ girls in my class. My "
          "brother is ___3___ years old. There are ___4___ students in our school.",
        a=["twenty", "twelve", "ten", "twenty"],
        s=("are / There / ten / boys / .", "There are ten boys.", ["There are ten boys"]),
    ),
    ("3上", 11): dict(
        p="I have a ___1___. It is white and it can jump. A ___2___ is green and it lives near the "
          "water. A ___3___ can fly in the sky. A ___4___ can swim in the river.",
        a=["rabbit", "frog", "bird", "fish"],
        s=("can / A / fly / bird / .", "A bird can fly.", ["A bird can fly"]),
    ),
    ("3上", 12): dict(
        p="There are four seasons in a year. ___1___ is warm and flowers open. ___2___ is hot, and we "
          "go swimming. ___3___ is cool and leaves fall. ___4___ is cold, and we make snowmen.",
        a=["Spring", "Summer", "Autumn", "Winter"],
        s=("is / Spring / warm / .", "Spring is warm.", ["Spring is warm"]),
    ),

    # ==================================================== 三年级下册
    ("3下", 1): dict(
        p="I like colours. The sky is ___1___. The apple is ___2___. The banana is ___3___. The grass "
          "in spring is ___4___.",
        a=["blue", "red", "yellow", "green"],
        s=("is / The / blue / sky / .", "The sky is blue.", ["The sky is blue"]),
    ),
    ("3下", 2): dict(
        p="This is a lemon. It is ___1___. The candy is ___2___. The soup is ___3___. The medicine is "
          "___4___, but it helps me.",
        a=["sour", "sweet", "salty", "bitter"],
        s=("is / The / sweet / candy / .", "The candy is sweet.", ["The candy is sweet"]),
    ),
    ("3下", 3): dict(
        p="Listen! The music is very ___1___. The library is ___2___, so we must be quiet. I can "
          "___3___ a bird singing outside. What a nice ___4___!",
        a=["loud", "quiet", "hear", "sound"],
        s=("can / I / a / hear / bird / .", "I can hear a bird.", ["I can hear a bird"]),
    ),
    ("3下", 4): dict(
        p="We go to the zoo today. A ___1___ is big and strong. A ___2___ has long hair around its "
          "head. A ___3___ can climb trees. An ___4___ has a long nose.",
        a=["tiger", "lion", "monkey", "elephant"],
        s=("can / A / climb / monkey / trees / .", "A monkey can climb trees.",
           ["A monkey can climb trees"]),
    ),
    ("3下", 5): dict(
        p="I have many ___1___. My favourite is a red ___2___. My sister has a ___3___. In the park we "
          "fly a ___4___ together.",
        a=["toys", "ball", "doll", "kite"],
        s=("has / My / a / sister / doll / .", "My sister has a doll.",
           ["My sister has a doll"]),
    ),
    ("3下", 6): dict(
        p="For breakfast I eat ___1___ and drink ___2___. At lunch I have ___3___ and some ___4___. "
          "They give me energy.",
        a=["bread", "milk", "rice", "juice"],
        s=("like / I / bread / .", "I like bread.", ["I like bread"]),
    ),
    ("3下", 7): dict(
        p="My ___1___ is swimming. I can ___2___ well in the pool. My friend can ___3___ and ___4___ "
          "very well, too.",
        a=["hobby", "swim", "dance", "draw"],
        s=("can / I / swim / .", "I can swim.", ["I can swim"]),
    ),
    ("3下", 8): dict(
        p="Today is my ___1___. I am nine years old. There is a big ___2___ on the table. I blow out "
          "the ___3___. My parents give me a nice ___4___.",
        a=["birthday", "cake", "candles", "present"],
        s=("is / Today / my / birthday / .", "Today is my birthday.",
           ["Today is my birthday"]),
    ),
    ("3下", 9): dict(
        p="We visit a ___1___ today. A ___2___ gives us milk. A ___3___ says “Quack, quack!” A "
          "___4___ is white and its wool is soft.",
        a=["farm", "cow", "duck", "sheep"],
        s=("is / The / on / cow / farm / the / .", "The cow is on the farm.",
           ["The cow is on the farm"]),
    ),
    ("3下", 10): dict(
        p="I like this ___1___. It is very ___2___. The cat has ___3___ eyes, and the mouse is ___4___. "
          "I laugh a lot.",
        a=["cartoon", "funny", "big", "small"],
        s=("is / The / funny / cartoon / .", "The cartoon is funny.",
           ["The cartoon is funny"]),
    ),
    ("3下", 11): dict(
        p="Today is ___1___ Day. I make a ___2___ for my mother. I give her a red ___3___. I say, “I "
          "___4___ you, Mum!”",
        a=["Mother's", "card", "flower", "love"],
        s=("love / I / my / mother / .", "I love my mother.", ["I love my mother"]),
    ),
    ("3下", 12): dict(
        p="The three pigs build three ___1___. The first one is made of straw. The ___2___ cannot blow "
          "down the ___3___ house. I like this ___4___ very much.",
        a=["houses", "wolf", "strong", "story"],
        s=("pigs / Three / build / houses / .", "Three pigs build houses.",
           ["Three pigs build houses"]),
    ),

    # ==================================================== 四年级上册
    ("4上", 1): dict(
        p="Today is the first day of school. I ___1___ a new ___2___ in the classroom. Her name is "
          "Jill. We say “___3___!” to our teacher, and she says “Good ___4___!” to us. Everyone is "
          "happy to be back.",
        a=["meet", "classmate", "Welcome", "morning"],
        s=("to / Nice / you / meet / .", "Nice to meet you.", ["Nice to meet you"]),
    ),
    ("4上", 2): dict(
        p="I can ___1___ in the pool, but I cannot ___2___. My sister can ___3___ English songs. My "
          "brother can ___4___ on the ice.",
        a=["swim", "skate", "sing", "skate"],
        s=("you / Can / swim / ?", "Can you swim?", ["Can you swim"]),
    ),
    ("4上", 3): dict(
        p="“Are you ___1___?” “No, I am ___2___. I have a lot of homework.” At noon I feel ___3___, so "
          "I have lunch. After a long walk I am ___4___ and want to sleep.",
        a=["happy", "sad", "hungry", "tired"],
        s=("you / Are / happy / ?", "Are you happy?", ["Are you happy"]),
    ),
    ("4上", 4): dict(
        p="___1___ you have any ___2___? Yes, I have two. My ___3___ has a little girl, and my ___4___ "
          "has a boy. They are my cousins.",
        a=["Do", "cousins", "aunt", "uncle"],
        s=("have / you / Do / cousins / any / ?", "Do you have any cousins?",
           ["Do you have any cousins"]),
    ),
    ("4上", 5): dict(
        p="My best friend is ___1___; she always helps others. She is ___2___ and learns quickly. She "
          "is ___3___, and she is not afraid of anything. She is ___4___, too; she helps me with my "
          "homework.",
        a=["kind", "clever", "brave", "helpful"],
        s=("is / My / kind / friend / .", "My friend is kind.", ["My friend is kind"]),
    ),
    ("4上", 6): dict(
        p="My mother is a ___1___. She works in a hospital. My father is a ___2___ at a school. My "
          "aunt is a ___3___; she looks after patients, too. My uncle is a ___4___; he drives a bus.",
        a=["doctor", "teacher", "nurse", "driver"],
        s=("is / My / a / father / teacher / .", "My father is a teacher.",
           ["My father is a teacher"]),
    ),
    ("4上", 7): dict(
        p="This is our school. We read books in the ___1___. We play football on the ___2___. We have "
          "PE lessons in the ___3___. The teachers work in the ___4___.",
        a=["library", "playground", "gym", "office"],
        s=("in / We / the / read / library / .", "We read in the library.",
           ["We read in the library"]),
    ),
    ("4上", 8): dict(
        p="Let's go to the ___1___. I want to ___2___ a pencil. It is only two yuan, so it is very "
          "___3___. That big toy is eighty yuan; it is too ___4___.",
        a=["shop", "buy", "cheap", "expensive"],
        s=("is / The / cheap / pencil / .", "The pencil is cheap.", ["The pencil is cheap"]),
    ),
    ("4上", 9): dict(
        p="Our home has four rooms. We cook in the ___1___ and take a shower in the ___2___. I sleep in "
          "my ___3___. On Saturday I help my mother ___4___ the house.",
        a=["kitchen", "bathroom", "bedroom", "clean"],
        s=("I / the / clean / kitchen / .", "I clean the kitchen.", ["I clean the kitchen"]),
    ),
    ("4上", 10): dict(
        p="There is a ___1___ ___2___ my home. The bus stop is ___3___ the shop. The garden is "
          "___4___ the house and the school.",
        a=["park", "near", "behind", "between"],
        s=("is / There / a / park / near / my / home / .", "There is a park near my home.",
           ["There is a park near my home"]),
    ),
    ("4上", 11): dict(
        p="Look at the picture. The sun is a ___1___. The window is a ___2___. The roof looks like a "
          "___3___. I can see a ___4___ in the sky.",
        a=["circle", "square", "triangle", "star"],
        s=("is / The / a / sun / circle / .", "The sun is a circle.", ["The sun is a circle"]),
    ),
    ("4上", 12): dict(
        p="It is a ___1___ day. We can play outside. Yesterday it was ___2___, so we stayed at home. "
          "Today it is ___3___; my kite flies high. Look at the sky; it is ___4___ and grey.",
        a=["sunny", "rainy", "windy", "cloudy"],
        s=("a / It / is / sunny / day / .", "It is a sunny day.", ["It is a sunny day"]),
    ),

    # ==================================================== 四年级下册
    ("4下", 1): dict(
        p="Touch the toy. It is ___1___. Touch the desk. It is ___2___. The wall is ___3___. The glass "
          "is ___4___.",
        a=["soft", "hard", "rough", "smooth"],
        s=("is / The / soft / toy / .", "The toy is soft.", ["The toy is soft"]),
    ),
    ("4下", 2): dict(
        p="I can ___1___ the flowers. They smell ___2___. I can ___3___ the soup. It tastes ___4___. "
          "This fish smells bad!",
        a=["smell", "nice", "taste", "nice"],
        s=("smell / The / nice / flowers / .", "The flowers smell nice.",
           ["The flowers smell nice"]),
    ),
    ("4下", 3): dict(
        p="___1___ at the picture. I can ___2___ a big tree. The sun is ___3___, and the room is "
          "___4___, so I turn on the light.",
        a=["Look", "see", "bright", "dark"],
        s=("can / I / a / see / tree / .", "I can see a tree.", ["I can see a tree"]),
    ),
    ("4下", 4): dict(
        p="My favourite ___1___ is English. I like ___2___ because I can read stories. In ___3___ I "
          "draw pictures. I am good at ___4___.",
        a=["subject", "English", "Art", "Maths"],
        s=("is / My / subject / English / favourite / .", "My favourite subject is English.",
           ["My favourite subject is English"]),
    ),
    ("4下", 5): dict(
        p="I like ___1___. I play it with my friends after school. My sister plays ___2___. My father "
          "plays ___3___ in the park. We all like ___4___.",
        a=["football", "basketball", "badminton", "volleyball"],
        s=("play / I / football / .", "I play football.", ["I play football"]),
    ),
    ("4下", 6): dict(
        p="I can play the ___1___. My sister plays the ___2___. My friend plays the ___3___, and he "
          "also plays the ___4___ in the school band.",
        a=["piano", "violin", "guitar", "drums"],
        s=("play / I / the / can / piano / .", "I can play the piano.",
           ["I can play the piano"]),
    ),
    ("4下", 7): dict(
        p="I ___1___ at six thirty every day. I have ___2___ at seven. After school I do my ___3___. "
          "At nine I go to ___4___.",
        a=["get up", "breakfast", "homework", "sleep"],
        s=("up / I / get / at / six / .", "I get up at six.", ["I get up at six"]),
    ),
    ("4下", 8): dict(
        p="On ___1___ I have a music lesson. On ___2___ I play football. On ___3___ we have a short "
          "school day. On ___4___ I stay at home with my family.",
        a=["Monday", "Wednesday", "Friday", "Sunday"],
        s=("is / Today / Monday / .", "Today is Monday.", ["Today is Monday"]),
    ),
    ("4下", 9): dict(
        p="I have a friend in ___1___. She lives in a big ___2___. Last week I wrote her a ___3___. "
          "Next year she will ___4___ Shanghai.",
        a=["Australia", "country", "letter", "visit"],
        s=("is / She / in / Australia / .", "She is in Australia.", ["She is in Australia"]),
    ),
    ("4下", 10): dict(
        p="There is a small ___1___ behind my house. We ___2___ flowers there. My mother gives the "
          "plants water, and they ___3___ fast. Now there is a red ___4___ near the wall.",
        a=["garden", "plant", "grow", "flower"],
        s=("grow / Plants / fast / .", "Plants grow fast.", ["Plants grow fast"]),
    ),
    ("4下", 11): dict(
        p="It is ___1___ Day. We have a ___2___ in the classroom. Some students ___3___ songs, and "
          "others play ___4___. Everyone is ___5___.",
        a=["Children's", "party", "sing", "games", "happy"],
        s=("are / We / happy / .", "We are happy.", ["We are happy"]),
    ),
    ("4下", 12): dict(
        p="The little duck is ___1___ and grey. Other animals laugh at it. In spring it grows into a "
          "white ___2___. Now it is very ___3___. The ___4___ teaches us not to judge by looks.",
        a=["ugly", "swan", "beautiful", "story"],
        s=("is / The / beautiful / swan / .", "The swan is beautiful.",
           ["The swan is beautiful"]),
    ),

    # ==================================================== 五年级上册
    ("5上", 1): dict(
        p="What will you be in the ___1___? I want to be a ___2___ and fly a plane. My friend wants to "
          "be a ___3___ and make nice food. We all have a ___4___.",
        a=["future", "pilot", "cook", "dream"],
        s=("want / I / to / a / be / pilot / .", "I want to be a pilot.",
           ["I want to be a pilot"]),
    ),
    ("5上", 2): dict(
        p="I go to school by ___1___. My sister goes by ___2___; it is very fast. My home is near, so "
          "I sometimes ___3___ to school. My father ___4___ his bike to work.",
        a=["bus", "underground", "walk", "rides"],
        s=("go / I / to / by / school / bus / .", "I go to school by bus.",
           ["I go to school by bus"]),
    ),
    ("5上", 3): dict(
        p="My birthday is in ___1___. It is the first month of the year. My mother's birthday is in "
          "___2___. My father's birthday is in ___3___. My sister's birthday is in ___4___, near "
          "Christmas.",
        a=["January", "May", "October", "December"],
        s=("is / My / in / birthday / May / .", "My birthday is in May.",
           ["My birthday is in May"]),
    ),
    ("5上", 4): dict(
        p="On Saturday we ___1___ my ___2___ and ___3___. They live in the countryside. We stay for "
          "the ___4___ and have dinner together.",
        a=["visit", "grandpa", "grandma", "weekend"],
        s=("visit / We / my / grandparents / .", "We visit my grandparents.",
           ["We visit my grandparents"]),
    ),
    ("5上", 5): dict(
        p="Tom is my ___1___ friend. We play ___2___ every day. He always ___3___ his toys with me. A "
          "good friend is someone you can ___4___ everything with.",
        a=["best", "together", "shares", "share"],
        s=("is / He / best / my / friend / .", "He is my best friend.",
           ["He is my best friend"]),
    ),
    ("5上", 6): dict(
        p="Look! My mother is ___1___ dinner. My father is ___2___ his car. My sister is ___3___ TV. "
          "I am ___4___ my parents with the housework.",
        a=["cooking", "washing", "watching", "helping"],
        s=("is / My / cooking / mother / dinner / .", "My mother is cooking dinner.",
           ["My mother is cooking dinner"]),
    ),
    ("5上", 7): dict(
        p="We are at the ___1___. The ___2___ is blue. I play with the ___3___ on the beach. I find a "
          "beautiful ___4___ near the water.",
        a=["beach", "sea", "sand", "shell"],
        s=("at / We / the / are / beach / .", "We are at the beach.",
           ["We are at the beach"]),
    ),
    ("5上", 8): dict(
        p="We have an ___1___ on Sunday. It is a school ___2___. We will ___3___ some food for a "
          "___4___ in the park.",
        a=["outing", "trip", "bring", "picnic"],
        s=("bring / Please / some / food / .", "Please bring some food.",
           ["Please bring some food"]),
    ),
    ("5上", 9): dict(
        p="Excuse me, where is the ___1___? It is next to the ___2___. I want to see a film at the "
          "___3___. The train ___4___ is over there.",
        a=["museum", "hospital", "cinema", "station"],
        s=("is / Where / the / museum / ?", "Where is the museum?", ["Where is the museum"]),
    ),
    ("5上", 10): dict(
        p="The ___1___ is strong today. It can ___2___ my hat away. Yesterday it was a ___3___ wind, "
          "and the leaves moved slowly. A ___4___ wind can make big waves.",
        a=["wind", "blow", "gentle", "strong"],
        s=("The / is / strong / wind / today / .", "The wind is strong today.",
           ["The wind is strong today"]),
    ),
    ("5上", 11): dict(
        p="We use ___1___ every day. We ___2___ it, wash with it and cook with it. But fresh water is "
          "limited, so we must ___3___ it. Turn off the tap and ___4___ water at home.",
        a=["water", "drink", "save", "use"],
        s=("must / We / water / save / .", "We must save water.", ["We must save water"]),
    ),
    ("5上", 12): dict(
        p="___1___ can be dangerous. It can ___2___ paper and wood. We must be ___3___ with matches. "
          "If there is a fire, call for help at once and stay ___4___.",
        a=["Fire", "burn", "careful", "safe"],
        s=("is / Fire / dangerous / .", "Fire is dangerous.", ["Fire is dangerous"]),
    ),

    # ==================================================== 五年级下册
    ("5下", 1): dict(
        p="Let's ___1___ the room. This ball is ___2___, and that kite is ___3___. The red bag is "
          "___4___, but where is mine?",
        a=["tidy", "mine", "yours", "hers"],
        s=("is / This / mine / ball / .", "This ball is mine.", ["This ball is mine"]),
    ),
    ("5下", 2): dict(
        p="Welcome to our new home. We watch TV in the ___1___. We have dinner in the ___2___. I like "
          "the ___3___ because I can see the garden. Dad keeps his car in the ___4___.",
        a=["living room", "dining room", "balcony", "garage"],
        s=("is / This / living / our / room / .", "This is our living room.",
           ["This is our living room"]),
    ),
    ("5下", 3): dict(
        p="What will life be like in the ___1___? Maybe a ___2___ will do the housework. Maybe we will "
          "travel into ___3___. Every ___4___ will help us work faster.",
        a=["future", "robot", "space", "machine"],
        s=("will / Robots / help / us / .", "Robots will help us.", ["Robots will help us"]),
    ),
    ("5下", 4): dict(
        p="___1___ is fun. I read a ___2___ every week. My father reads a ___3___ every morning. When "
          "I meet a new word, I look it up in a ___4___.",
        a=["Reading", "story", "newspaper", "dictionary"],
        s=("is / Reading / fun / .", "Reading is fun.", ["Reading is fun"]),
    ),
    ("5下", 5): dict(
        p="What do you do at the ___1___? I go to the ___2___ with my friends. My mother goes "
          "___3___ for food. After that we have a ___4___ at home.",
        a=["weekend", "cinema", "shopping", "rest"],
        s=("do / What / at / you / the / do / weekend / ?",
           "What do you do at the weekend?", ["What do you do at the weekend"]),
    ),
    ("5下", 6): dict(
        p="The summer ___1___ is coming. We ___2___ to go to Beijing. We will ___3___ by train and "
          "stay in a ___4___ near the park.",
        a=["holiday", "plan", "travel", "hotel"],
        s=("to / We / plan / travel / .", "We plan to travel.", ["We plan to travel"]),
    ),
    ("5下", 7): dict(
        p="Today is our ___1___. Parents come to school at nine. We ___2___ them at the gate. Then we "
          "put on a ___3___ in the hall. My ___4___ takes many photos.",
        a=["Open Day", "welcome", "show", "parents"],
        s=("to / Welcome / our / school / .", "Welcome to our school.",
           ["Welcome to our school"]),
    ),
    ("5下", 8): dict(
        p="Can I help you? I want to buy a coat. What ___1___ are you? I am medium. Please ___2___ it "
          "on. It ___3___ you well. How much is it? The ___4___ is 200 yuan.",
        a=["size", "try", "fits", "price"],
        s=("it / Can / try / I / on / ?", "Can I try it on?", ["Can I try it on"]),
    ),
    ("5下", 9): dict(
        p="I feel sick today. I have a ___1___ and a bad ___2___. The doctor gives me some ___3___ and "
          "tells me to have a good ___4___.",
        a=["fever", "cough", "medicine", "rest"],
        s=("have / I / a / fever / .", "I have a fever.", ["I have a fever"]),
    ),
    ("5下", 10): dict(
        p="Paper is a great ___1___. The Chinese ___2___ it long ago. ___3___ is another important "
          "invention; it helps us read and learn. Every ___4___ changes our life.",
        a=["invention", "invented", "Printing", "invention"],
        s=("is / Paper / great / a / invention / .", "Paper is a great invention.",
           ["Paper is a great invention"]),
    ),
    ("5下", 11): dict(
        p="The Spring ___1___ is the most important Chinese festival. We eat ___2___ and watch the "
          "dragon dance. At the Mid-Autumn Festival we eat ___3___ and look at the moon. During the "
          "Lantern Festival we carry a ___4___.",
        a=["Festival", "dumplings", "mooncakes", "lantern"],
        s=("eat / We / dumplings / .", "We eat dumplings.", ["We eat dumplings"]),
    ),
    ("5下", 12): dict(
        p="A ___1___ has a beautiful ___2___. He builds a high ___3___ around it. Spring, summer and "
          "autumn come and go, but the giant feels cold. When he opens the wall, every ___4___ comes "
          "back to his garden.",
        a=["giant", "garden", "wall", "season"],
        s=("has / The / a / giant / garden / .", "The giant has a garden.",
           ["The giant has a garden"]),
    ),

    # ==================================================== 六年级上册
    ("6上", 1): dict(
        p="I am ___1___ up now. I am ___2___ than last year. My face has ___3___, too. When I was "
          "little, I could not ride a bike; now I can. People ___4___ all the time, and change is part "
          "of life.",
        a=["growing", "taller", "changed", "change"],
        s=("am / I / taller / than / before / .", "I am taller than before.",
           ["I am taller than before"]),
    ),
    ("6上", 2): dict(
        p="Last summer I ___1___ to Hainan with my parents. We ___2___ in a hotel near the sea. I "
          "___3___ my grandparents for a week. We had a wonderful ___4___.",
        a=["went", "stayed", "visited", "holiday"],
        s=("went / I / to / Hainan / .", "I went to Hainan.", ["I went to Hainan"]),
    ),
    ("6上", 3): dict(
        p="To be ___1___, we need good ___2___. I do ___3___ for thirty minutes every day. I always "
          "eat vegetables. Good ___4___ are hard to build, but they keep us well.",
        a=["healthy", "habits", "exercise", "habits"],
        s=("is / Exercise / good / for / us / .", "Exercise is good for us.",
           ["Exercise is good for us"]),
    ),
    ("6上", 4): dict(
        p="Our new ___1___ is very ___2___. She often helps us. Everyone in the ___3___ likes her. "
          "When someone is in trouble, we ___4___ each other.",
        a=["neighbour", "friendly", "community", "help"],
        s=("is / Our / friendly / neighbour / .", "Our neighbour is friendly.",
           ["Our neighbour is friendly"]),
    ),
    ("6上", 5): dict(
        p="Many wild animals are in ___1___. The giant ___2___ is one of them. We must ___3___ them and "
          "their homes. Never buy things made from ___4___ animals.",
        a=["danger", "panda", "protect", "wild"],
        s=("must / We / animals / protect / .", "We must protect animals.",
           ["We must protect animals"]),
    ),
    ("6上", 6): dict(
        p="I have an ___1___ in Canada. We write ___2___ to each other every week. The ___3___ makes "
          "it easy to talk. I like my ___4___ because we share the same interests.",
        a=["e-friend", "emails", "Internet", "e-friend"],
        s=("have / I / an / e-friend / .", "I have an e-friend.", ["I have an e-friend"]),
    ),
    ("6上", 7): dict(
        p="Let's go to the ___1___ this evening. The new ___2___ is very ___3___. I have two "
          "___4___, so we can sit together.",
        a=["cinema", "film", "funny", "tickets"],
        s=("go / Let's / the / to / cinema / .", "Let's go to the cinema.",
           ["Let's go to the cinema", "Let us go to the cinema"]),
    ),
    ("6上", 8): dict(
        p="Last Saturday we ___1___ the science museum. We learned a lot about ___2___. There was an "
          "interesting ___3___ about space. I want to ___4___ again next month.",
        a=["visited", "history", "exhibit", "visit"],
        s=("the / We / museum / visited / .", "We visited the museum.", ["We visited the museum"]),
    ),
    ("6上", 9): dict(
        p="Beijing is the ___1___ of China. It is a ___2___ city with a long history. The Great Wall "
          "is a famous ___3___ there. Every year many people ___4___ this great ___5___.",
        a=["capital", "famous", "building", "visit", "city"],
        s=("is / Beijing / capital / the / of / China / .", "Beijing is the capital of China.",
           ["Beijing is the capital of China"]),
    ),
    ("6上", 10): dict(
        p="We cannot see ___1___, but we need it. Plants and animals need clean air to ___2___. Today "
          "there is too much ___3___ in some cities. We should keep the air ___4___.",
        a=["air", "breathe", "pollution", "clean"],
        s=("need / We / air / clean / .", "We need clean air.", ["We need clean air"]),
    ),
    ("6上", 11): dict(
        p="___1___ are our friends. Each ___2___ makes oxygen for us. We can make paper and furniture "
          "from their ___3___. On Tree Planting Day we plant new trees to protect our ___4___.",
        a=["Trees", "leaf", "wood", "planet"],
        s=("give / Trees / us / oxygen / .", "Trees give us oxygen.", ["Trees give us oxygen"]),
    ),
    ("6上", 12): dict(
        p="The ___1___ is our home. It is a beautiful blue ___2___. We must ___3___ it. Do not throw "
          "___4___ on the ground, and use less plastic.",
        a=["Earth", "planet", "protect", "rubbish"],
        s=("is / The / our / Earth / home / .", "The Earth is our home.",
           ["The Earth is our home"]),
    ),

    # ==================================================== 六年级下册
    ("6下", 1): dict(
        p="Jill and I are very ___1___ in some ways. We are ___2___ good at English. But we are "
          "___3___ in one way: her favourite ___4___ is music, and mine is sport.",
        a=["similar", "both", "different", "hobby"],
        s=("are / We / both / good / at / English / .", "We are both good at English.",
           ["We are both good at English"]),
    ),
    ("6下", 2): dict(
        p="Our lives have ___1___ a lot. In the ___2___, people wrote letters. ___3___ they send "
          "emails. Life is faster now, and every ___4___ brings something new.",
        a=["changed", "past", "Now", "change"],
        s=("have / Our / changed / lives / .", "Our lives have changed.",
           ["Our lives have changed"]),
    ),
    ("6下", 3): dict(
        p="What will our school be like in the ___1___? Maybe every ___2___ will have a ___3___. "
          "Students will ___4___ at home on rainy days. But we will still need friends.",
        a=["future", "classroom", "computer", "learn"],
        s=("will / We / computers / use / .", "We will use computers.",
           ["We will use computers"]),
    ),
    ("6下", 4): dict(
        p="I love ___1___. My favourite ___2___ is Qi Baishi. He used a ___3___ and black ink. Look "
          "at the colours in this ___4___; they are so alive.",
        a=["art", "artist", "brush", "painting"],
        s=("is / My / artist / favourite / Qi Baishi / .", "My favourite artist is Qi Baishi.",
           ["My favourite artist is Qi Baishi"]),
    ),
    ("6下", 5): dict(
        p="In the craft lesson we make a paper flower. You need ___1___, ___2___ and ___3___. Cut the "
          "paper first, then glue it. Our ___4___ look beautiful.",
        a=["paper", "scissors", "glue", "crafts"],
        s=("make / We / a / paper / flower / .", "We make a paper flower.",
           ["We make a paper flower"]),
    ),
    ("6下", 6): dict(
        p="I like ___1___ lessons. Last week we had a ___2___ on the playground. I can ___3___ very "
          "high. Our class worked as a ___4___ and won.",
        a=["PE", "race", "jump", "team"],
        s=("like / I / PE / lessons / .", "I like PE lessons.", ["I like PE lessons"]),
    ),
    ("6下", 7): dict(
        p="We should ___1___ others when they are in ___2___. Last month I was a ___3___ at the "
          "library. Helping people makes me feel ___4___.",
        a=["help", "need", "volunteer", "good"],
        s=("help / Let's / others / .", "Let's help others.", ["Let's help others"]),
    ),
    ("6下", 8): dict(
        p="Look at the ___1___. It says “No Smoking”. This ___2___ is important. Every rule ___3___ "
          "something. The ___4___ is over there, next to the stairs.",
        a=["sign", "rule", "means", "exit"],
        s=("does / What / sign / this / mean / ?", "What does this sign mean?",
           ["What does this sign mean"]),
    ),
    ("6下", 9): dict(
        p="We can ___1___ old things. I use a plastic ___2___ to hold pens. My mother makes a bag "
          "from ___3___. In this way we make less ___4___.",
        a=["reuse", "bottle", "plastic", "rubbish"],
        s=("can / We / things / reuse / .", "We can reuse things.", ["We can reuse things"]),
    ),
    ("6下", 10): dict(
        p="This ___1___ is about a brave girl. The main ___2___ is clever and kind. The ___3___ "
          "wrote it in 1900. The ___4___ is exciting from the first page.",
        a=["storybook", "character", "author", "plot"],
        s=("is / The / exciting / story / .", "The story is exciting.",
           ["The story is exciting"]),
    ),
    ("6下", 11): dict(
        p="At ___1___ people decorate a tree and give presents. At ___2___ children wear strange "
          "clothes and ask for sweets. At Thanksgiving families eat ___3___ and ___4___ pie.",
        a=["Christmas", "Halloween", "turkey", "pumpkin"],
        s=("is / Christmas / a / festival / .", "Christmas is a festival.",
           ["Christmas is a festival"]),
    ),
    ("6下", 12): dict(
        p="There are five ___1___ in a ___2___. They sit inside and talk about their ___3___. Each pea "
          "has a different wish. In spring they ___4___ into new plants.",
        a=["peas", "pod", "wishes", "grow"],
        s=("grow / Peas / in / spring / .", "Peas grow in spring.", ["Peas grow in spring"]),
    ),
}
