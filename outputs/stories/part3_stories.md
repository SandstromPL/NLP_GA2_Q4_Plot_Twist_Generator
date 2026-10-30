# Part 3: decoding-strategy comparison: all generated continuations

Everything inside a quote block is **model-generated and unedited** (detokenised from the saved tokens). Failed, repetitive and incoherent outputs are included on purpose. Source: `outputs/generations/*.jsonl`.

## P3_mystery (a mystery)

**Opening (human-written):** The detective entered the abandoned house and noticed that every clock had stopped at exactly midnight. Suddenly, the telephone rang...

Prompt words outside the RNN/LSTM vocabulary (seen as `<unk>`): detective

### Vanilla RNN

**greedy, seed 0** (85 tokens, stop: eos)

> The bird was very sad and scared. The bird was scared and didn't know what to do. He tried to get the ball, but he couldn't find it. He tried to get the ball, but it was too late. He was so sad and he couldn't wait to play with his friends. He was so happy and thanked the man. He thanked the man and said, "thank you, mommy!"

**greedy_rep1.2, seed 0** (132 tokens, stop: eos)

> It was a big, scary monster! The bird was very sad because he wanted to go on an adventure. So, he decided to take a nap in his pocket. But then, something bad happened. The little boy saw a big tree with lots of leaves. Timmy loved to play with his toys all day long. One day, tim's mom asked him to help her find a new toy. Lily said yes and they went to the store. She found some yummy snacks and put them in a bowl. "Look, mommy! I'm going to get my ball!" she exclaimed. "You're welcome, lily. You are very kind."

**temp_0.5, seed 0** (39 tokens, stop: eos)

> The frog was gone. His mom told him that it was not important to share his toys and not to worry. He said he could have a new friend and he was very proud of him.

**temp_0.5, seed 1** (44 tokens, stop: eos)

> The bird flew away. The bird was so happy. The bird had a lot of fun. The little girl was so happy to have her new friend. The little girl was so proud of herself for being so brave.

**temp_0.5, seed 2** (150 tokens, stop: max_len)

> The bird was very sad and sad. The cat said, "I'm sorry, I'm sorry. I didn't mean to break the dog. It's a toy. It's not to be sad." the little girl was very excited and she ran to the room. She saw a big, scary cat. It was a big, shiny flower. She wanted to make it, but she was very upset. She asked her mom, "what's wrong?" her mom replied, "I'm sorry, lily. I was wrong." lily felt sad and sad. She asked her mommy, "mommy, can I play with your toy?" her mom said, "yes, I want to catch it." lily was so

**temp_0.5, seed 3** (150 tokens, stop: max_len)

> The bird started to panic. The bear was scared. He wanted to go on the slide. He tried to reach it, but it was too late. The man was very sad and he wouldn't have any money. Timmy was sad and didn't know what to do. He tried to climb the tree, but he couldn't reach it. He didn't know what to do. He asked his mommy, "what is that?" lily asked. "I'm going to make a big mess!" she said. "I'll help you." lily was excited to help her mom. She put on her shoes and went to the store. She saw a big, round ball. She wanted to show it to her mom. She took

**temp_0.5, seed 4** (24 tokens, stop: eos)

> The bird flew away. It was a big, scary ball. The cat was very happy and had a great time.

**temp_0.8, seed 0** (74 tokens, stop: eos)

> Then he saw the way back in the water. The fox was so proud of himself and he started to cry. He knew he had to do it to tell his mom quickly. They both put the ball on the wide plane and turned the water back. They were so happy! From bob was on the other side, he felt so happy and content. The end.

**temp_0.8, seed 1** (150 tokens, stop: max_len)

> The bear realized the frog was too slow. He tried to open it, but he didn't know what to do. Suddenly, something strange happened. Tim looked around and saw a big tree with his friends. He wanted to play with it, but he didn't mind how to fix it. Timmy didn't want to use this ball, so he said, "don't worry, I'll help you." his mom smiled and said, "that's gifted fake! That is so cool." and she was so happy. She was so happy that she thanked mom for giving her how to pick it up. Her mom got happy and didn't know how to make it and say hello. Her mommy said, "my name is your brother

**temp_0.8, seed 2** (59 tokens, stop: eos)

> The bird was very hurt and sad. The mechanic said, "it's okay. I should be kind and help me." the boy nodded and said, "of course, you can be friends." the king was happy to hear his mom and they both loved him. The end.

**temp_0.8, seed 3** (33 tokens, stop: eos)

> The ground started to be scared. The lion felt bad and thanked the librarian. The man kept the little boy and never never the nightmare again when he was now.

**temp_0.8, seed 4** (22 tokens, stop: eos)

> Suddenly, the sky turned shiny and faster than it. The little girl was so happy and proud of herself.

**temp_1.0, seed 0** (143 tokens, stop: eos)

> Then he saw the way back in the middle. Jack didn't want to stop playing with the balloon. But no one didn't budge. He dropped the rock in his pocket and stepped back to the top of the wide maze. When he was done, he threw off the fence and bob sat down for a warning. Then he pushed the meat and started to zip the present pose. So, he used to load his swimsuit and he shared them with his mouth. As she sang, she would feel in her neighbor's hair forever. The boy was so happy! The big bird ran back to mailing with the youth. And he shared his yard. He really pulled with joy in it and all the funny animals.

**temp_1.0, seed 1** (143 tokens, stop: eos)

> The bear realized the wind was wobbly to get free. The bird had become a scarf and but the key was stuck. The next day, the stream was the worst last time before making a mess so. He wasn't happy to find out what he was allowed. Suddenly, a rock appeared and timmy fell down. So, this time not want to swim. The orange truck liked to move. The lion jumped through the pond and tried to chew it back. Then the boy was so scared, he couldn't wait to give it back to the man. He learned that he should always listen to your parents and not work about those of things for others to say sorry to his friends and say goodbye to everyone again.

**temp_1.0, seed 2** (133 tokens, stop: eos)

> The bird picked up the mouse and jumped over it. The puppy became back on the slide and flew away from his nest. He turned around and saw some old trees. Tim wanted to play at the ground, so he put the key in his pocket and ran home quickly. He was so proud of itself for being so helpful and impressed. He started to cry and happy to be safe, but his leg would get dark. The elephant grabbed the block to the edge of the barn. Suddenly, it started to rain! The water was too weak to catch the jam. The cheese was happy to know that it's important to be safe and continued to play together.

**temp_1.0, seed 3** (150 tokens, stop: max_len)

> The ground started to be scared in the air. Timmy was scared, but he did not wrong. He pulled up a cloth and started rocking when tom didn't find a rock. Timmy asked his mommy, "can you teach me how to lend my candle?" his mommy smiled and said, "I know we was scared. On the puppy with my project, I can't hear him." jill and leo walked back to their homes with the toy. The monster had a fun day with the number of garden at the park. He was so happy to see the sun like his village. It was still tired because he was comfy again. He was sure to make her feel called of better. So, the little teacher hopped around the store,

**temp_1.0, seed 4** (150 tokens, stop: max_len)

> Suddenly the fire jumped into shiny pieces and stood in the sun. Joe was so surprised and sad. He had an idea. But his mom called him to keep him. He said it was too dangerous. His owner took him to the store where was hidden to the park. Inside was a sweet treat, even if tim was alive. It seemed curious, but it thought it was too expensive. He picked it up and started to laugh, but it was weird. His mom was playing in the room she saw a photo of freeze yet with to wash her turn rolling through. His mom sadly in the kitchen and thought about to stop writing. Timmy got sad and didn't want to buy lily anymore. Lily ran to the house and saw a dog struggling

**temp_1.2, seed 0** (150 tokens, stop: max_len)

> Then he saw the way his ball back. He knew that being persistent meant and brought true foods's room. No one knew it croaked, but then something heard happened. Bobo was very happy! He thanked the bug and missed the ball after friends. "Goodbye for happiness safety!" bob was so excited that he forgot and sang so much fun! Eventually, the skeleton johnny pose and keeping playing with their bucket. Jay went to the bathroom, and he thanked the old bear that was filled a lot of fun sunny of the interesting apples. He sang up and then soaring over the stairs. Dotty was upset again before taking his pan with his friends. Acorns woke up with her small sack and licks the boat tightly. After they finished, she hugged back

**temp_1.2, seed 1** (150 tokens, stop: max_len)

> The bear realized the wind was wobbly to get free. The bird had become a scarf and but the key was okay. And what somebody did now, tim and his mom met him timmy to dad his example food. Later that day, timmy's knee showed timmy at her how she thought it was timmy. Timmy started so soft. Tom did not mind his ball's joke and sam wanted his wagon. He wished the red white flowers he could chew on it. Then he sailed that it hurt mine. "And I'm sorry I left juice and you too fast for you. Do you want to remember him?" max reaches for of branch from a tree. He checks his box and says, "okay, pirate?" mom said. Mom gives

**temp_1.2, seed 2** (85 tokens, stop: eos)

> The bird picked up the mouse and jumped in it. The puppy became back on the wife and flew home from his grandma. Mom turned a blanket and packages for a while. When her mom told her she had painting to sally, it was old screaming, but the crown didn't work. Mittens was sad because she was worried. Losing replied, "here, mia! Jane agreed., she juice ok very possible."

**temp_1.2, seed 3** (150 tokens, stop: max_len)

> Everywhere it started to be scared in the air. Timmy was amazed who wanted to build back. "I know this though would you go?" tom looked surprised, a coach at the sky and a new box. The naughty puppy was delighted and nodded he went for bed and did not know how boat it was made. Joe did on a puppy with his masterpiece, but he couldn't do that. Jill tried to untie her luckily he couldn't chase it. Janey felt scared. She felt helpless. Her mommy said, "well, thank you for saving me. Your mom will help him help it scare me. Then we can bake fruits together." jane was very excited! Called the lady saw that her journal gather marble on lily's arm.

**temp_1.2, seed 4** (150 tokens, stop: max_len)

> Suddenly the fire jumped into shiny pieces and stood in the sun. Joe arrived, ready for his staff. When it was a rug, it came out of the farm. The fish and the rabbit followed even around it. Every day, the most known would make flowers all day long. One day, lily mentioned to wear her finger hands and pray. "You really thought it was a moment. I should carry myself now for music, don't have fun." mick had crying and was running by she saw who had broken freeze yet with to wash her disappointment rolling through. She welcomed sadly in the wild box and down to find some new animals. She waved her fingers every day, and it was even better. The winter monkey arriving stayed around into

**topk_10, seed 0** (150 tokens, stop: max_len)

> Then he saw the mess. It was a big truck that was broken. It looked so nice that he was scared and didn't know what to do. He wanted to try it, but his mommy told him not to worry. He said, "don't worry, timmy!" she said. Timmy was sad. He asked him, "what should I have the best? I will get the ball. You are a big bird!" he said. The man said that was very kind and said he needed to help them go away. He said, "I'm sorry, I wanted to see the bird too and my little brother," he said. He picked up the stick and said, "thank you, mommy." the little

**topk_10, seed 1** (37 tokens, stop: eos)

> The bear felt the wind blowing in the sky. The bird was so thankful to its friends. The man was so glad and couldn't wait to play with the ball. The end.

**topk_10, seed 2** (150 tokens, stop: max_len)

> The bird was very sad and sad. Then he heard a voice. It was a big, scary lion. His friend was scared, but he wanted to stay too. Tim wanted to play with his toys, but he was sad. He asked if he wanted to play with the truck. But the man said, "okay, but only if you're not safe." timmy's parents said yes and said, "let's go!" lily said, smiling. "Thank you, mommy!" her mom said, "no, you can't go on the couch." she went to her house and found a big box on a bench. She picked it up and put some of the soap inside in a bowl. Then he added a

**topk_10, seed 3** (109 tokens, stop: eos)

> The bird started to panic! The bear was very angry and scared. He wanted to help. "I know, I'll help you!" the little boy was excited to go to the beach. He ran to the pond and saw the little girl. She was so happy and hugged him tightly. She was so proud of her work and the big bear had a great time. From that day on, lily always made sure to always ask her friends to play on the wall. She felt so lucky that she had found something new for her.

**topk_10, seed 4** (140 tokens, stop: eos)

> Suddenly the boat stopped. It was the most beautiful thing in his mouth. The cat saw the ball and was curious. Tim wanted to play with the ball, but the man said "no, I need to eat it for you," said the old man. The rabbit thought for a moment and said "I want to play with it." "okay, mommy." the boy thanked the little boy and said, "thank you!" they both went to the store and gave him some bread and cookies. Tim smiled and said to lily, "I love you too, lily. You are very brave and smart." the little boy was happy that he could have fun with it.

**topk_40, seed 0** (150 tokens, stop: max_len)

> Then he saw the mess. It was a funny dog. It was friendly and shiny and he wanted to catch a tree! It broke from the ceiling and broke it with a hat. It was loud and scary. Lily was sad and angry. She said, "sorry, lily. She did not mean to hurt. And I'm sorry for you. I told you to listen to her and be careful. You are a big knight." sara and ben nod. She hugs him. "You helped me stay away from the fountain." tom says. They sit on the grass and go outside. The car goes and goes on the floor. It is hard to make a mess! They cannot reach the top, behind a big puddle. It

**topk_40, seed 1** (66 tokens, stop: eos)

> The bear realized the wind was in the middle of the forest. All of a sudden, two the owl stopped working. The dog had fallen down and down the road. The bird flew away and he was sad. He said, "thank you!" timmy was happy to have his family and they all had a great time.

**topk_40, seed 2** (150 tokens, stop: max_len)

> The bird was very sad and sad. Then he heard a voice. Tim was scared. He dropped the knife from in his mom and went to see it. Tim hugged tim and sam. At the barber, lily and max were playing with a big, brown worm. He said, "hey, why are you going to share a story with you?" mia says. She puts on her hand and goes to her bike. She wants to try to grab the cat on her neck. She wants to pet the bird with the balloon. She thinks it was a good idea. She picked out the soup and took it to her mom. When they found the book, they saw a nice cat. She wanted to catch it. She said she wanted

**topk_40, seed 3** (150 tokens, stop: max_len)

> The ground started to be scared in the air. Timmy was scared, but he did not want to break the lion. Timmy was scared of how he didn't find a rock. So he reached a trap and climbed away. His friend and asked him what was wrong, and decided to play together again. Timmy agreed to show it on his own friends. But when he got back outside, he decided to try a special walk from he saw. He ran to the window and grabbed a deep breath. He asked his mom if they could go. So they did it, and it looked like a toy car. They decided to pick some fruits and vegetables from the house. The little girl said, "that looked like a new way to go."

**topk_40, seed 4** (40 tokens, stop: eos)

> Suddenly the fire jumped into it. The truck looked very sad. Her friends tried that the mean had had broken and it started to rain again. They all laughed and continued to walk around the yard.

**topp_0.9, seed 0** (124 tokens, stop: eos)

> Then he saw the way back in the middle. Jack didn't want to stop playing with the balloon. But no one didn't budge. He dropped the rock in his pocket and stepped back to the top of the pond. The ball couldn't believe his eyes! Wally had lots of fun he was scared but he wanted to try out, but the mean bird told the people to get out and take her help. The little girl was sad, but he knew the old bear was wearing a scary piece of ice cream. From that day on, he would remember to bring his words and make sure to stay organized before.

**topp_0.9, seed 1** (69 tokens, stop: eos)

> The bear realized the wind was wobbly to get free. The bird had become a big and friendly cat. Timmy ran back home and said, "thank you for lending me the sheep. I'm so happy!" the tree was very angry and he showed his cat to his home. He thanked timmy and brought his energy back to the creek.

**topp_0.9, seed 2** (150 tokens, stop: max_len)

> The bird picked up the mouse and jumped over it. The puppy looked around and saw many things, and when his friend was getting there, he noticed something strange! He couldn't find it to stay up. The other kids had lots of fun in the snow, and he couldn't wait to ride it in his backyard. The fish walked back to the rock and looked at the toy, she felt so very proud of her. She grabbed the book to the edge of the barn and she smiled. "Thank you, sally. I love you." her mom said, "sure, lily, don't worry, thank you." tim replied, "don't worry, I will stay in the sink in my garden." he was so

**topp_0.9, seed 3** (150 tokens, stop: max_len)

> The ground started to be scared. But it was too hard to go inside. But the storm was hot and flew up to the house. When tom looked up, he saw a huge little bird. Sue was so scared that she went closer to play. She was scared and decided to pull down the seed. So, she went on a chair with a round bird on the table. Her mum smiled and said, "I'm glad you are going to climb back." bob and her mom played on the swings and went to the post office. They did not see the chicken again. Lily was sad. She knew she was right. She felt sorry for breaking her bag. She said, "that was a charming teacher! Lily said."

**topp_0.9, seed 4** (150 tokens, stop: max_len)

> Suddenly, the sky turned behind a huge hole and the sun was gone. The deer saw the cave and was curious. Tom was very brave and he started walking. The children laughed and clapped its hands. His parents flew in and hugged him. The old man smiled and said, "let's leave it around." he pointed to a tree and decided to try to write it. When he arrived, he saw a little boy in his den. Timmy felt scared and had never seen anything as he could find. The puppy ran fast with to wash his hands, but it was too late. Timmy was sad but he said he had to behave. His mom made him angry and said, "no, I don't know you can't help you

**topk_40_rep1.2, seed 0** (150 tokens, stop: max_len)

> Then he saw the mess his ball back when he came out of him. Then, a kind fox named sammy went to the store to play with it. Lily was curious but timmy didn't know what you needed. Timmy was sad because he could not reach the bird or the park. Bob wanted to make something special. Later that day, jimmy's owner took him home outside to get her passport. They both got angry and threw it into a spot. He gave them carefully to him some tools for jack. "Where did it go away?" timmy nodded eagerly. He looked around and saw lots of people, so one morning came at tim. He couldn't figure any new friends! All the kids were amazed, they knew how many fun things

**topk_40_rep1.2, seed 1** (76 tokens, stop: eos)

> It was too big for them to help. He grabbed some sticks all away at the side of the cage, but tim and his family were very sad because the cake made the mess out what happened - there couldn't keep trying on its eyes. The bird said goodbye, and soon his dog flew back with his owner so much that he did not mind any harm's life earlier.

**topk_40_rep1.2, seed 2** (42 tokens, stop: eos)

> "Hello! I have a surprise for you. It's time to go on. Maybe we can play more later soon." from then on, lily always sat with her friend and shared their bags together.

**topk_40_rep1.2, seed 3** (17 tokens, stop: eos)

> They both started to play it in. So the family played together all day long.

**topk_40_rep1.2, seed 4** (14 tokens, stop: eos)

> She was scared of her friends's head from a deep hole again.

### LSTM

**greedy, seed 0** (130 tokens, stop: eos)

> It was a big, scary monster. The bear was scared and he ran away. The bear was scared and he wanted to help. He ran to the door and saw the bear. He was so excited! He ran to the door and saw a big, scary bear. The bear was scared and ran away. The bear was scared and he ran away. The bear was very sad. He wanted to help the rabbit. He asked his mom if he could go to the hospital. The doctor said yes, but the rabbit was too scared. He was very sad. He was very sad. He wished he had been able to help the rabbit.

**greedy_rep1.2, seed 0** (137 tokens, stop: eos)

> It was a big, scary monster! He ran to his mom and asked, "what is this?" the voice replied, "I'm going to take a nap." the little girl smiled and said, "yes, I can help you." the little girl was so excited. She wanted to try something new. But then, she saw a big, scary dog. The dog was scared of the dog's tail. The cat looked sad and scared. The dog chased her and the dog ran away. The dog was very happy. He hugged the dog and thanked him for being brave. From that day on, the dog was always careful when playing with his friends.

**temp_0.5, seed 0** (137 tokens, stop: eos)

> It was a big, scary monster! The crocodile was very scared and he ran away. He was scared and scared. He wanted to be brave and explore the world. But then, something strange happened. The hunter looked around and saw a big, old man. He had never seen anything like it before. He was so scared that he ran towards the old man. The man looked around and saw a big, black dog. He was so scared that he started to cry. The boy was scared and he ran away. The man was very sad. He wished he had been brave and wanted to stay away. The little boy was happy and he knew he had to be careful.

**temp_0.5, seed 1** (150 tokens, stop: max_len)

> It was a big, scary dog. The mouse was scared and wanted to go on the other side of the fence. The dog had seen the ball and the dog was very sad. He ran around the house and saw the dog. The dog was very angry and scared. The dog wanted to help the dog, so he wanted to help. He said, "don't worry, I will help you." the dog smiled and said, "no, it's very dangerous. It will be bad and be lonely." the little fish nodded and said, "I will help you. Let's go to the park and play with the dog." the bird looked at the toy and said, "it will be fun. You can fly

**temp_0.5, seed 2** (150 tokens, stop: max_len)

> It was a big, furry cat. The cat had a big smile on its face. The cat was so scared that it had seen a big hole in the sky. The little kitten was scared, but the cat was scared. The poor cat was scared. The cat wanted to help. The bird said, "don't worry, I'll be here." the kitty agreed and they both went to the garden. They saw a little girl who was very sad. She wanted to help the bird, so she said, "I'm sorry, I'm sorry. You should be careful." the little girl nodded and said, "I'm sorry, dad. I was just joking. I'm glad you could help." the little girl

**temp_0.5, seed 3** (149 tokens, stop: eos)

> It was a very sad, but the child was too scared. The old man smiled and said "I'm sorry, but I want to play with you." the little girl was very excited and said, "yes, I will help you." the little girl and the boy ran to the store and bought a big bag on the ground. He was so happy that he jumped up and down and said, "I'm so glad you're able to do it!" and the little girl was so happy. She thanked the little girl for being so brave and brave. The little girl was so happy and thanked the old man for being so helpful. She had been able to do something special and that she had made a wonderful friend.

**temp_0.5, seed 4** (150 tokens, stop: max_len)

> It was a big, shiny cat! The cat was so excited. It looked like a big tree. The cat was scared and wanted to help the bird. The bird said, "don't worry, little bird. I will help you." the bird looked at the cat and said, "I am sorry, I'm sorry. I will help you." the bird looked at the bird and said, "I'm sorry, mommy. I'm sorry I had to be afraid of the bird." the bird smiled and said, "you can play with the bird in the park." the bird nodded and said, "yes, you can do it." the bird and the bird played together every day and had a great time

**temp_0.8, seed 0** (150 tokens, stop: max_len)

> It was a big, weak monster! The crocodile was very scared and hurt. He tried to open the box but he was too fast. He dropped the jet and jumped quickly. He was scared, but he didn't want to leave the big tree. He cried and shook his head against his nose. But then, he heard a voice. The kitten said, "I don't know, I'm sorry. I won't hurt you." the monkey was sad, but he was a bit fearful. He was very sad and wanted to go to the store. He reached out and caught out of the bird. The cat was scared and ran away from the mouse. The bear felt very lucky. He had been sick and he was glad to

**temp_0.8, seed 1** (150 tokens, stop: max_len)

> It bent down to see what it was. He grabbed a shock, and threw it to his mom. But then, something spooked happened. A big red voice came out of the house and asked his mom why she was going to get the candy. The man was angry and said, "don't worry, my mommy. This is not a toy." the old lady smiled and said, "I'm sorry, my mom said." mum gave the truck fake head and it was gone. "This is my mom and dad explained," she said. "I'll be careful with your bed." the little girl nodded and ran to the store. Mama looked at the stamp and watched her mommy all around the house. Mum said,

**temp_0.8, seed 2** (150 tokens, stop: max_len)

> It was a big surprise! It was a big, black puppy. It was a big, brown spider! The puppy was terrified, so he wanted to stay in the garden for a long time. The frog slowly walked closer to the poor old man, feeling the brave eagle who could hear the sound of the birds going down. But the fox started to cry. The boy gave the rabbit a hug and said, "let's go see what I can't." the man was relieved and he smiled back. He said, "I want to put the worm back first." the child smiled and said, "thank you, farmer. You are very brave." the duck was grateful for the dove in his hand. Then he was able

**temp_0.8, seed 3** (70 tokens, stop: eos)

> Everywhere it started to be different in the air. The sun was shining and the sky was orange. The words had never seen before and the sun was shining. It was bigger and brighter! It had two green colours and ladders. The sun made a big bed and it was so pretty! She smiled and waved goodbye to the girl on her face.

**temp_0.8, seed 4** (77 tokens, stop: eos)

> Suddenly the fire began to stop john and john looked around, feeling a bit weak, but he had to leave. It started to rain again and the water kept on the floor. It was too hard for his powerful crayon and that, until there was no more peoples. The boat was gone, but it was too late. The hands had to unlock, and it was gone forever.

**temp_1.0, seed 0** (138 tokens, stop: eos)

> It was a farmer. His dad saw what made him angry. He asked his mom who he was doing and doing him! His picture was very angry and he wanted to know if he was doing the volcano. He looked around and found a big pot of wood for someone safety! From bob was so scared that he forgot that he had lost his daughter. Daddy told the present to end the scarves and they found a few games. He shared them with his wife, and she was passing fast. Finally, he returned the brown pillow and the boy was so happy! The big brother ran back to mailing jail again, but and only soon he was smarter even more than he tried in it!

**temp_1.0, seed 1** (145 tokens, stop: eos)

> It bent down to see what it belonged. He grabbed some energy all all around outside and tiptoed inside. But he did not talk to anyone! He was so happy and started to cry. Then he heard a voice. "Hey, that's the cabin! You stole this wings!" jen was so surprised. So she hugged her arm. Then she grabbed the orange and put her bandaid clean the milk with the red white pile of lemons from the box. Then the little bee asked, "what is this?" mom smiled. "It's too heavy for you." the bear nodded, and then handed it to his mom. From that day on, mama made sure to keep them by her mommy's visit!

**temp_1.0, seed 2** (150 tokens, stop: max_len)

> It was getting weak. He was excited and he quickly grabbed it. He stood and looked in the air and his mouth. He turned around and saw some children playing with questions. Suddenly, the water caught a large cardboard hill. It was coming from a hut, and he couldn't wait to catch it. Karen was worried that losing the banana started to get back. Jane gave the pig some juice and taught them what was well. But soon, the doorbell stayed above the lock. Suddenly, it started to freeze! Molly said, "you remember what you did. You could come out first step after you, mommy!" every day, mandy found her dad to make him sweep. She saw the dove in a puddle and then said: "

**temp_1.0, seed 3** (116 tokens, stop: eos)

> Everywhere it started to be different in the world. The sun was hot and they all jumped on the hot pie. It never covered all of the different colours now. A girl was so happy! The two friends were so excited because the sun could play in the sun. And did not know how to use the red cushions, it on a puppy with another masterpiece. Every night it was a song. It was a fantastic thing, and robert with its work. Janey felt happy. She could feel the mirror of her veil soundly, and her parents read they to enjoy the sun.

**temp_1.0, seed 4** (150 tokens, stop: max_len)

> Suddenly the fire began to stop john and john looked around, feeling a bit weak, but he had to leave. It started to rain again and the water kept crying. The first shrimp was safe and even stopped to close anymore. "Hey I don't know,". Inside his parents, "please". "He could never go to school, you weren't hurt us," he said. Joseph slowly tried again and he gave the hands to his mom. His mom said, "stop, mummy. Our apology will surrender attention to others. I think we're too bowing sadly in the wild line." the customers got angry and stood on the ground. The boat jumped up and the head ran away. Grandpa was so excited. He

**temp_1.2, seed 0** (150 tokens, stop: max_len)

> Popcorn lay down and started his vacation back. Between the sunshine, all one answered, who demanded that the storm touched; spring was fragile, but then something heard the noise quickly. It was a loud noise outside from wide, smaller light! Molly couldn't believe what she had excitedly. She wanted her mother in warning. And nothing out, then something happened. How curl the pose may find something useful, there was all bright and white! Mama asked: "mommy, can that my avocados would happen in the sunny place where it go?". Mama nodded its head, keeping mike mad and enjoy the patient before she was only waiting at it. Emma woke up with her mom and felt very old. She started wearing more and more others all over

**temp_1.2, seed 1** (150 tokens, stop: max_len)

> It bent down to see what it belonged. He grabbed some energy all feet at the side but then he stopped moving. The chickens erupted louder and held up the ink. The sheep smelled bad and so there couldn't keep appear on its truck. He slowly pulled out of his wings and scurried into the desk before his angry trouble. He noticed that he had broken his favourite truck. There were letters racing pounding people through his pocket when he heard a voice. The truck was very surprised, with everybody with a stern wing. It cost shouting for joining around the dragon for scaring. Taylor jumped up and looked out of the shadows. There of branch for a long time, - he smiled and then thanked him for being so loyal. Welcomed never mentioned to curl

**temp_1.2, seed 2** (91 tokens, stop: eos)

> Stitch was so weak that he shook her hands and added him was a cell thunderstorm. He couldn't follow his neighbor walked up, but he couldn't find them. He poked his best speed at the ground, painting and ignoring. In poor day, a feeling, brave soldier walked beside. The pen said goodbye, going to imagine a few daisies started dinner, even happy when he stopped, spinning his differences beat. Everywhere was well, it seemed block!

**temp_1.2, seed 3** (150 tokens, stop: max_len)

> Everywhere it started math. One year. So the cell find a fake pair of bits back. "I know this whole would dream," when the tv opened it a rock. It looked super a trap just like the naughty white same hand. Janey touched the noise, and did not know what boat was? Then, a gentle on lightning, with another masterpiece, worse, were salty to move against it and a group of courage he saw with its lines. Janey felt scared, and she quickly marched down the garden at the same direction of the day they did. When it was time to go home, gus stopped playing. The calmer was warm and the sadness were gone that was called the bank. Grandpa looked around and comforted john proudly. This time

**temp_1.2, seed 4** (150 tokens, stop: max_len)

> Suddenly the fire jumped into shiny pieces and everyone looked about work. Grace arrived, ready for her staff. When it was a rug, it would come into the farm where everyone had shrimp. Nora followed even tugged it with time that, until there was hidden to work.. Inside was a sweet cold bus around the park. It moved around and curious, feeling really happy and content. Maddy practiced with her boat on the stage and milly added anything to pick. She was happy to be like a pastel artist by joining the broken pattern yet everyone to wash her. Happiness had a lot of fun in the wild gym but she made all energy when she got off. Then alex heard being really big and happy. He saw the winter monkey arriving - toed into

**topk_10, seed 0** (142 tokens, stop: eos)

> It was a big, strong monster! The animal had been walking away from a nearby place, and the bear was scared! He quickly stepped closer and saw a friendly rabbit. He was very surprised. He said "hey, where are you? I'm looking for something else!" bob was so scared that he wanted to try. He ran towards the bird with the mouse and it jumped in the ground. The bear was so angry! He ran around the house and watched the butterfly flutter. He smiled and said, "thank you, rabbit." the mouse was so happy and hopped away with the rabbit. He was so happy and grateful. He learned to be more careful and never take the fox.

**topk_10, seed 1** (119 tokens, stop: eos)

> It was too big for them. The family was scared! He had to go outside and go inside. But he did not listen. The other animals were so happy. The family started to cry. The children were scared but they didn't want to stay back at the same place. The kids did not think that was a lot of fun. Then, they heard a loud noise. It was the sound of the sky. The people were sad. They had made a big mistake. The people were so relieved that he had taken the fire and they would never forget the day. The end.

**topk_10, seed 2** (150 tokens, stop: max_len)

> It was getting closer. He was excited and he quickly grabbed it. He took it out and saw what was happening in his mouth. He looked everywhere but he couldn't find it. It was getting bigger than any other kids. It was a big, scary, strong animal who was scared of the lion. The farmer was scared but he was determined to get back out of the cave, but his mom said that it was okay. The little boy said he couldn't believe it. The little boy smiled and said, "thank you for helping me. You are my best friend," the bear replied. The rabbit smiled and said, "thank you, mommy. You're my best friend." the old bear felt better and said, "

**topk_10, seed 3** (100 tokens, stop: eos)

> The people started to panic! Suddenly, the wind blew and the wind was gone. The child was very scared but sad. The little girl was scared, so her mother said no. "Don't worry sweetheart," her father said. "That's ok, but you have to be patient and be careful. You can't be a very little girl." the little girl was so excited. She hugged her mum and said, "I'm okay. I'll never forget this day."

**topk_10, seed 4** (123 tokens, stop: eos)

> It was a big, scary cat! The kitten said, "let's go play with it. It will be fun now!" the dove was so happy. The cat said "look, the bird can have fun and have fun. I'll stay in the water." the worm was excited and decided to take a nap. It flew down, and it flew up high in the grass. The sky was very hot and the water were blue. Soon, it had lots of fun. The bunny was so happy to have made a big, fluffy bunny. The bird was happy to have a new friend.

**topk_40, seed 0** (150 tokens, stop: max_len)

> It was a big, strong monster! Mama went to pick up the puppy and brought it to the door. A giant man appeared in a big bag. He said, "please, I will help you get your money in the cage!" the old man took off the hat and ran away. Mommy was sad. Then the old man's daughter heard a voice: "don't worry, I'll help you. I will have some cake and food." mummy carefully said, "a piece of my clothes will help them go." he smiled and wiped the big bite off his hands. When the man was ready out of his work, he gave his mom some delicious cream and a surprise. Mommy said, "it was a fun day

**topk_40, seed 1** (122 tokens, stop: eos)

> It was too big for them. The family was scared! John had swum at the hospital but then he stopped working. The next day, he went to the park to play with his ball. He was so excited. He ran back and ran to the hill. Suddenly, he saw a boy. The man saw him who wanted to see what he had. He grabbed a ball and began to cry. His mom got angry and tried to help him. The truck was very angry. It had frozen in and looked forward. After that, he had to give up. He felt very brave and safe again.

**topk_40, seed 2** (150 tokens, stop: max_len)

> It was getting weak. He was excited and he quickly grabbed it. He tried and ran and laughed and shouted his hands. He couldn't believe his eyes. The 3 - year - old nodded, asked him why he was there. The old man explained that he was just 3 years - and was able to do it. The little boy was angry and asked why the boy gave them some candy. The boy was relieved. He started eating and more, until he saw a man. A big, three year old boy pointed over and smiled at them. "You did you see my dad's grandma," the mommy explained. "What is going there here?" john was curious. He saw the fire in a corner. Then he remembered his

**topk_40, seed 3** (132 tokens, stop: eos)

> Everywhere it started to be different in the world. The sun was hot and they all jumped on the table. Suddenly, a gentle little scared came down from the sky. Everyone was so happy! The two friends were so excited and went to the zoo. They waved goodbye and smiled as they reached the top of the forest. Then on they had an idea. They went on an adventure to the zoo and stayed together. They were amazed at all the amazing plants. After a minute, the family would come back soon at the park for the beach for they to go inside and explore the village. It was still a bit fun and would never forget the day.

**topk_40, seed 4** (150 tokens, stop: max_len)

> Suddenly the fire began to rain. The truck looked like a perfect castle. So, the family had an idea. It started to move from the boat. The ship started to rain and the rain was scared. It flew into the sky until there was a new place. It was no longer frustrated. It was filled with joy, so it seemed to stay alone in the sky. James wanted to climb on the boat now, but he was too tight. He grabbed his helmet and said, "stop! That is our best!" but it was still too dangerous. The children were not scared. But now the boat said, "don't forget you. You need to take things not go to sleep, but it's safe. If you want

**topp_0.9, seed 0** (78 tokens, stop: eos)

> It was a farmer. His dad saw what was happening and decided to take a nap. He stepped closer and touched the ground. Suddenly, he heard something loud. He quickly fell asleep. Everything was filled with lots of sand. The sailor was scared, so he ran away. From then on, the hero was known and he knew he'd always be a very naughty place to end.

**topp_0.9, seed 1** (113 tokens, stop: eos)

> It was too big for them. The creature was gone! He had swum at the hospital but then he stopped moving. The chickens had fallen down and blocked the ring away. He looked everywhere but he was gone. He followed the king and he couldn't believe what it was going. He heard a terrible whisper. He cried. He noticed that he had been trying to complete his missing home. The lion put the broken white pile of places in his pocket and then hurried off to fix it. He found them that he just bit right away and bob was safe.

**topp_0.9, seed 2** (150 tokens, stop: max_len)

> It was getting weak. He was excited and he quickly grabbed it. He stood and looked in the air and his mouth. He turned around and saw something. The pipe was so big that it had drawn a large cardboard hill. It was coming from a hut, quickly just up on the water! It was very relieved and stepped on the grass. Jake ran back to his eyes and stayed safe. After a few seconds, the elephant grabbed the block, and filled up the lock. Suddenly, he heard a loud bark. The rope was singing and it was a deep star. He ran out of the house and found his favourite fork! When he found the book, he was able to stay in the chamber in a huge cave. He was so

**topp_0.9, seed 3** (64 tokens, stop: eos)

> Everywhere it started to be different in the world. The sun was hot and they all jumped on the hot pie. It made the house scared when they looked so cool. Everyone laughed and giggled as the two players were so happy. The sun made their favourite bed sparkle, and the dust was even more easy than playing.

**topp_0.9, seed 4** (150 tokens, stop: max_len)

> Suddenly the fire began to stop, and everyone looked around, feeling a bit weak, but it had no way. It started to rain again and the water kept crying. The first shrimp was safe and even stopped to close the box, until there was no more flowers. The train was gone, but it seemed to be safe, so it seemed to get down in the sky. James wanted to climb on the boat, but he didn't want to get off. His mom was so happy and he couldn't believe the broken freeze before but he had to turn away. John felt scared and alone. But then, he heard a noise. He got closer and closer. The boat jumped up and the head ran away. He was so excited that he

**topk_40_rep1.2, seed 0** (150 tokens, stop: max_len)

> It was a big, strong monster! Mama went to pick up her puppy and brought him some of the vegetables in the oven. She tried to copy the answer but then it was time for him to reach again. But he didn't want to be sad and cried. The little penguin ran away and tried to get back home. So, he started eating a big smile instead of noise. Finally, they found a few white spot outside from a nearby tree. The old bear said, "look what you have done talking and it is very important." henry saw the spider's tail and wanted to catch the bird better and he kept its eye. He soon pulled out some small pieces and put the net in his bag. His mom smiled as she

**topk_40_rep1.2, seed 1** (150 tokens, stop: max_len)

> It was too big for them to help. So danny saw his mom's mom outside and hugged him. She ran over and said, "now I have the cake!" mommy smiled and said: "of course I do!" they ran to the kitchen with her blanket, grabbed a cup of chocolate and started to use. Finally, they got up - fived their luggage. There were lots of things with the red balloons in the sky and were both big singing in the sun. Dad had never found this before. He wanted to make something beautiful too. Mama smiled. She told his mom about him and her work. As she walked around the park, he heard some noise and ran outside to play again. His mother saw him on to hear

**topk_40_rep1.2, seed 2** (63 tokens, stop: eos)

> It was getting weak. He was excited and he quickly grabbed his favorite shirt on. He used the string to make a castle for him. He felt so proud of himself. When he got to the barber, the king was there. They all loved making a new friend for who was going outside in the water.

**topk_40_rep1.2, seed 3** (150 tokens, stop: max_len)

> Everywhere it started to be different in the world. The sun was hot and they all jumped on a little bit of a noise. When they got home, the man heard that his face looked around and saw all the children. He smiled and asked him what was wrong. As she walked closer to the children, john was scared. He saw his friends walking into the farm, carrying them up the street and running away. He waved goodbye so he could hardly believe it. The kids were amazed by how he asked other questions when they found their language for jack to join him and explore his village. It was still looking for something important. After his family was over, he knew it wouldn't forget. So, the 3 year old smiled sadly. "

**topk_40_rep1.2, seed 4** (137 tokens, stop: eos)

> Suddenly the fire began to rain, and everyone looked like a perfect castle. Alice was thrilled! She asked her mother what a kind of child would come into the farm where the teacher said they had finished. Jane showed grandma how that, she needed it. Alice wanted the idea and smiled with pride for being so brave. When it moved around, lucy's friends had to be able to make all sorts of things on the stage. She added some glue - crayons to take, ready and mix a bunch butter by sugar. Jill ran out with her fingers, carefully, and grabbed lots of colorful colours. But now, she made all sorts of animals and different memories - games every day!

## P3_discovery (a surprising discovery)

**Opening (human-written):** While digging in the garden, Ben found an old wooden box. When he opened it, he could not believe his eyes.

Prompt words outside the RNN/LSTM vocabulary (seen as `<unk>`): none

### Vanilla RNN

**greedy, seed 0** (150 tokens, stop: max_len)

> He was so excited! He ran to the edge of the hill and saw a big, scary dog. He was so excited! He ran to the edge of the hill and saw a big, scary dog. He was so excited! He ran to the edge of the hill and saw a big, scary dog. He was so excited! He ran to the edge of the hill and saw a big, scary dog. He was so excited! He ran to the edge of the hill and saw a big, scary dog. He was so excited! He ran to the edge of the hill and saw a big, scary dog. He was so excited! He ran to the edge of the hill and saw a big, scary dog. He was so

**greedy_rep1.2, seed 0** (73 tokens, stop: eos)

> He was so excited! He ran to the edge of the hill and saw a big tree with lots of leaves. Timmy wanted to play with it, but he didn't know what to do. Suddenly, he heard a loud noise coming from behind him. "Hey, I'm sorry, lily. You are my friend. I am glad you're safe."

**temp_0.5, seed 0** (75 tokens, stop: eos)

> He was so happy. His mommy said, "you're welcome, timmy. You are my best friend." the boy smiled and said, "I will help you." the little boy smiled and said, "thank you, lily. You are so smart and brave!" bob was so happy that he forgot to be so good for the rest of the day.

**temp_0.5, seed 1** (119 tokens, stop: eos)

> He bent down to see what it was. He asked his mom, "can I help you get the number?" the bird said, "yes, I know. I will be careful with his friends." the little girl was so happy to see her cat, but she knew she had to be careful. So, she decided to go to the park with her friends. She was so excited to have a new friend. She said goodbye to the big tree and sailed inside. She had so much fun playing with the dishes. She was so happy that she had found a new friend.

**temp_0.5, seed 2** (150 tokens, stop: max_len)

> He was so excited. He ran to the tree and saw a big, scary bird. The bird was so scared that he couldn't believe it. He tried to catch the bird, but it was too late. The next day, the little girl was feeling sad and didn't know what to do. She thought it was a fun day. She took the toy car and gave it to her mom. She was so happy to have her friend, so she went to the store and bought some yummy food. She said, "look, mommy!" she said. She looked around and saw a big, scary bug. She was so scared that she started to cry. "I'm sorry, lily," she said. "I'm so

**temp_0.5, seed 3** (66 tokens, stop: eos)

> He was so excited. He started to climb the hill and explore the world. But then he remembered the words and the water was gone. The boy was so happy to hear himself. He was so happy and thanked the wise owl. From that day on, lily always remembered to bring her toys to always play with her friends.

**temp_0.5, seed 4** (87 tokens, stop: eos)

> Suddenly, he heard a loud noise. He looked up and saw a big, scary bear. The bird was curious and wanted to have a closer look. The owner asked the cat to help him climb the tree. He said, "that's a great idea,". The boy was so happy and thanked the farmer for helping him. From that day on, timmy and his friends were all very happy and had lots of fun.

**temp_0.8, seed 0** (75 tokens, stop: eos)

> Suddenly, he heard a loud noise. It made him feel sad and hurt. He tried to open the box, but he didn't know what to do. He swam back to the house and closed his eyes. He was happy when he put the flower in the water and it made bob feel better. He was so happy and thanked the magician for being a good helper.

**temp_0.8, seed 1** (150 tokens, stop: max_len)

> The bear realized that it was important to be careful. Timmy stopped all his friends and ran away. He was very sad and couldn't wait to play with the ball. The next morning, timmy's mom said, "let's go outside and play with jam together," said his mommy. Timmy felt grateful for him and hugged him. "Thank you, timmy. I'm going to clean the tree with the red ball. He will be so brave and gifted for you that it will be proud of them." the little girl smiled and said, "that's great, lily. We can pick it together." lily nodded and said, "that's okay, lily and anna. You are happy." the prince was scared to hear

**temp_0.8, seed 2** (54 tokens, stop: eos)

> He was so excited. He ran to the tree and played with it. He learned that if he worked hard his friends would be even if he wears it, the winner would heal best things to stay in the sky and find a beautiful poor old tree. The end.

**temp_0.8, seed 3** (150 tokens, stop: max_len)

> He was so happy. One day, he saw a bird flying in the sky. He wanted to stand the melon, but the house was too heavy. Benny's friend said, "that's a trap! You need to be careful and cozy about your bed." and did not know what to do. Then, a little boy saw his friends and asked, "what are you doing here?" tommy asked. "I am sorry, I'm not mad. I demand and help you. I'm sorry at first, I'll help you tell me." and the boy said sorry to the boy and gave him a cup. His mum said, "I'm sorry, we should not go back to the museum!" max felt happy

**temp_0.8, seed 4** (150 tokens, stop: max_len)

> Suddenly, he heard a loud roar. He looked up and saw a big, round tree! The bird was curious and a bit scared. The man was very happy. He said it was time to go home, but he was afraid of the dark. He knew he had to do something sweet. But then he remembered he wanted to go to the park. It thought it was a moment. He thought it would be fun to learn, so he hopped off to take a closer look like a bird. He thought the water was very high and fun. Timmy's mom saw his work sadly in the kitchen. The cat said, "don't worry, I'll help you!" lily and mr, still saw a big monkey arriving. Lucy was

**temp_1.0, seed 0** (31 tokens, stop: eos)

> Suddenly he saw the way his ball and gave him a big hug. From then on, floppy's mom knew no one can happen picture of her things.

**temp_1.0, seed 1** (150 tokens, stop: max_len)

> The bear realized that it was dangerous to get up early! He had been so careful that but then he stopped working. And his family did not listen to the man. The owl looked at the doctor tree and said, "don't worry, the bird is gone, but I don't care. It's my so soft." "okay, but I can't get lost!" the bird stayed with the red white flowers and a big smile. Leo was so excited that he got into her warm and she scurried through the fields. He saw the dragon fly in circles. The girl asked, "mommy, max, can we watch a film?" john replied, "and then you must be happy with you!" she knew to herself

**temp_1.0, seed 2** (58 tokens, stop: eos)

> He stopped and heard the noise. He saw it and said, "don't worry, I'll follow my neighbor in my leg. I found a treasure. I want to get best in the water." the other kids had shared of fun things that they needed the best to help.

**temp_1.0, seed 3** (84 tokens, stop: eos)

> He was so itchy. One day, he saw a ball and watched he could build the top. He pulled up a cloth and started rocking when he looked so cool. He hopped around, but the lawyer just was so naughty. The sun could play in bed and watch and did not know what boat. He made his friends feeling happy and sad. He had a new friend and that they could always support him together.

**temp_1.0, seed 4** (150 tokens, stop: max_len)

> Suddenly, he heard a shiny pond and stood in the sun. Joe was so surprised and sad. He had an idea. But his mom called him to keep him. He said it was too dangerous. His owner took him to the store where was hidden to the park. Inside was a sweet treat, even if tim was alive. It seemed curious, but it thought it was too expensive. He picked it up and started to laugh, but it was weird. His mom was playing in the room she saw a photo of freeze yet with to wash her turn rolling through. His mom sadly in the kitchen and thought about to stop writing. Timmy got sad and didn't want to buy lily anymore. Lily ran to the house and saw a dog struggling

**temp_1.2, seed 0** (102 tokens, stop: eos)

> Suddenly he saw the way his ball and gave him a big man's mechanic. Paw felt sad that he knew no one want to go now. Then, he sat down quickly fell asleep. Everything could reach again! Wide missed the ball after a few seconds and johny off safety! From bob he was much hero warning. And the ball was very tall. Daddy told the present to always find something useful for help before eating games. He shared them; he was so happy that that was was a great time!

**temp_1.2, seed 1** (37 tokens, stop: eos)

> The bear realized the valuable lion had grown. He realised that he had to obey money and but the key was okay. And timmy had completed his unique party every day. The end.

**temp_1.2, seed 2** (46 tokens, stop: eos)

> Stitch was so weak. He shook her head and said, "it's okay. Maybe if we follow your neighbor in the door instead?" from sheep. Tim hugged questions for best that to stay safe and share and trustworthy.

**temp_1.2, seed 3** (64 tokens, stop: eos)

> Everywhere he started planting stretching one in the air thunder. At timmy, he heard all back. "I know this though never be scared of how caring or say it is bigger himself." but the lawyer just was still naughty. The sun could play in bed and watch and did not know how boat it was clear.

**temp_1.2, seed 4** (150 tokens, stop: max_len)

> Suddenly the pill jumped into shiny pieces and stood in the sun. Joe arrived, ready for his staff. When it was a rug, it came out of the farm. The fish and the rabbit followed even around it. Every day, the most known would make flowers all day long. One day, lily mentioned to wear her finger hands and pray. "You really thought it was a moment. I should carry myself now for music, don't have fun." mick had crying and was running by she saw who had broken freeze yet with to wash her disappointment rolling through. She welcomed sadly in the wild box and down to find some new animals. She waved her fingers every day, and it was even better. The winter monkey arriving stayed around into

**topk_10, seed 0** (150 tokens, stop: max_len)

> Suddenly he saw the big tree in the middle. Jack saw that his friends were playing with him's house. Timmy had a new toy, but he liked to play with his friends. But then, a little girl named tim went to the park. She saw a bird flying in the sky. It was a big, red ball. The bird was scared and wanted to take a look. Lily was scared. She wanted to take it back, but it was too fast. She was very happy. She went outside and saw something shiny in the grass. She saw the big bird and smiled and said, "hello, little bird. I have a special message to make you feel better!" the little girl was excited to have a new friend.

**topk_10, seed 1** (82 tokens, stop: eos)

> The bear felt sad for his new friend. He ran to his mom and said, "I want to make it." timmy and the bird went to the park and started to climb on the swings. As they were playing together, they saw a big hill with a big, blue balloon. Timmy was so happy to see that he had learned a valuable lesson that day - don't be rude and helpful.

**topk_10, seed 2** (62 tokens, stop: eos)

> He was so excited. He ran to the tree and saw a big tree on the ground. He wanted to climb in the sky, but he couldn't. The dog started to fall in the water. He felt very sad. He was so proud that he didn't know what to do. The end.

**topk_10, seed 3** (150 tokens, stop: max_len)

> He was so happy. It started to rot. The bird was scared and ran away. He had never seen anything like a star and wanted to play with the worm. He was so happy! He ran home. He ran to the house and found a shiny object. As he walked, she saw a man playing on a bench on a bench. He had a small toy truck that he could play with him. She put some dough on his head and said it was funny. She took the key back in the garden and started to laugh. Her mom smiled and said, "thank you for being honest," lily said. She was happy to hear that she had been able to keep her safe. Her parents smiled and said, "that's

**topk_10, seed 4** (82 tokens, stop: eos)

> Suddenly, he heard a knock on the floor and said, "let's go see the hill!" they all had a great idea. When they got home, the man said "let's go inside, it looks time." the boy was so happy and started to laugh. He ran home and played with his toys all day long. He knew he had to be careful when picking as he could.

**topk_40, seed 0** (77 tokens, stop: eos)

> Suddenly he saw the mess. It was a funny dog. It was friendly and shiny and he wanted to catch a tree! He picked it up and carried it to his friends. They both put the flag on the paper, and the door was delicious. They were so happy! From bob was on the other side, and the old man's friends were happy with the work together.

**topk_40, seed 1** (66 tokens, stop: eos)

> The bear felt sad for his owner to get up. Timmy was so excited to have the toy car. Timmy ran back and forth and looked very cold. The little girl wanted to help her dad so she ran by herself with the big eyes. The bird was so nice and she thanked the fairy. She had a wonderful time.

**topk_40, seed 2** (150 tokens, stop: max_len)

> He stopped and ran around and laughed. Then he heard a voice. Tim was scared. He dropped the knife from in his mom and went to see it. Tim hugged tim and sam. At the barber, lily and max were playing with a big, brown worm. He said, "hey, why are you going to share a story with you?" mia says. She puts on her hand and goes to her bike. She wants to try to grab the cat on her neck. She wants to pet the bird with the balloon. She thinks it was a good idea. She picked out the soup and took it to her mom. When they found the book, they saw a nice cat. She wanted to catch it. She said she wanted

**topk_40, seed 3** (150 tokens, stop: max_len)

> He was so happy. One day, he saw a ball and decided to play with the hoop. He pulled up a cloth and started running into the water. It was almost cold. He reached a new box. He ran to the top and saw a rabbit in his hand. He knew she could use the car to try it on it, so he asked her mom for help. Her mum smiled and said, "yes, I will make you feel better." lily gave tom some medicine. Tom asked her mom if they could go. So they did it, and lily looked at lily's car. "Lily, you found me! Can I have my doll?" her mom said, "that's a good way lily. This is

**topk_40, seed 4** (45 tokens, stop: eos)

> Suddenly, he heard a knock on the floor and said, "let's go over the hill. It will be fun now!" from that day on, lily loved to ride and dance whenever she had a new friend.

**topp_0.9, seed 0** (36 tokens, stop: eos)

> Suddenly, he heard a loud noise and gave him a big hug. From then on, floppy's mom knew that had a new picture of his things that he made more amazing.

**topp_0.9, seed 1** (34 tokens, stop: eos)

> The bear realized that it was dangerous to get up early! He had been so careful that his mom could come back. And she had completed the unique party ever since.

**topp_0.9, seed 2** (64 tokens, stop: eos)

> He stopped and heard the noise. He saw it and said, "don't worry, I'll follow my neighbor in my leg. I found a treasure. I want to get something else to stay." the other kids had shared of fun things, but the brave soldier was always careful and never got away again.

**topp_0.9, seed 3** (128 tokens, stop: eos)

> He was so happy. It started to drip the highest ball and watched it in the air. "I know this, would you go?" tom looked at her castle and said, "I am hungry and because I lost his hurt and I didn't know what to do." pete nodded and continued to walk to the park with his friends. He had a great time playing with the robot. He also took it home and he couldn't wait to climb back. The girl and her cat played on the swings and went to the post office. They did not see the chicken again. Lily was happy to have some cookies and candy.

**topp_0.9, seed 4** (150 tokens, stop: max_len)

> Suddenly, he heard a loud roar and stood in the sun. Joe was so surprised and sad. He had an idea. But his mom called him to keep him. He said it was too dangerous. His owner took him to the store. The old lady said yes. Jane smiled and said, "I love you too, lily. I'm proud of you for helping me." lily was so happy that she ran away, so she ran to find her mom, ready to go up the hill. Then she reached out and looked everywhere. But the elephant couldn't give up. When they were playing, lily said, "don't worry, lily. I'm being naughty." she said, "okay, mommy. I'm safe

**topk_40_rep1.2, seed 0** (25 tokens, stop: eos)

> Suddenly he saw a big tree in the middle of the lake. He asked his mom if they could keep it from him!

**topk_40_rep1.2, seed 1** (104 tokens, stop: eos)

> The bear felt sad for his owner to get up early! John had a lot of fun playing in the water near the ocean. But then something bad happened the little bird started to weep and the boy was gone. The tree flew away and timmy fell asleep anymore at her. She thought it sounded like the sun could make a new surprise. "Look, my favorite flower is very dirty!" the man put the red glass on it. From that day on, tom made sure it hurt someone with any other animals.

**topk_40_rep1.2, seed 2** (35 tokens, stop: eos)

> Suddenly, a big storm came by and saw he had left on it. John learned that if he worked hard his friends would be even better and I can stay to sleep.

**topk_40_rep1.2, seed 3** (60 tokens, stop: eos)

> At first, he saw that he was so excited. At timmy, he heard a voice. "I know this is here!" sam said. "Now it is bigger than yours!" lily and her mom tried to play with the toys all day long because they did not go home together.

**topk_40_rep1.2, seed 4** (88 tokens, stop: eos)

> Suddenly the boat jumped into a pond and stopped barking above him again. Timmy tried to catch it on it too hard. Tom was very mad when they started walking. The children laughed and clapped its hands. "It looks time that, two of three. We have all. But no one can do it! I want to fly so fast!" "you are my hero!" from then on, everyone always tried for food, so

### LSTM

**greedy, seed 0** (75 tokens, stop: eos)

> He was so excited! He ran to the kitchen and saw a big, round ball. He wanted to play with it. He ran to the slide and started to climb. He was so happy. He ran around the park and laughed. He was so happy. He had a great time. He was so happy. He had a great time playing with his new toy.

**greedy_rep1.2, seed 0** (82 tokens, stop: eos)

> He was so excited! He ran to the kitchen and saw a big, round ball. He wanted to play with it. But then, something bad happened. The rain started to move. The wind blew and the sky was too high. The little boy was scared and didn't know what to do. He tried to get out of the hole, but it was too late. He had been gone forever.

**temp_0.5, seed 0** (112 tokens, stop: eos)

> He was so excited. His mom said, "let's make it go." so, they went to the kitchen. It was a big, juicy rock. They were so excited. They played with the ball and laughed. When the sun was over, they went to the park. They saw a big tree. It was so high and tall. The sun was shining and it was very hot. It was so bright and pretty. Ben and his mom were very happy. They played together for a while, but then it was time to go home.

**temp_0.5, seed 1** (125 tokens, stop: eos)

> It was a big, round, round. He was so excited. He wanted to explore the world. But he did not know what to do. He looked around and saw a big tree. He was so excited. He ran to the garden and saw a big, round ball. He wanted to climb it. So, he asked his mom, "can I go inside?" his mom smiled and said, "yes, it is." they went to the park and saw lots of animals. They were so happy and excited. They played together every day. They played together every day. They were very happy.

**temp_0.5, seed 2** (111 tokens, stop: eos)

> He was so excited. He ran to the kitchen and saw a big, yellow bird. The bird was so happy. He wanted to play with it. He ran to the tree and tried to grab it. The bird was very happy and started to cry. The bird was sad. The bird was able to get the bird. But the bird was too late. The boy was very sad. He was very sad. He had been able to help the bird. The bird was still a little bird. He was happy that he had saved the bird.

**temp_0.5, seed 3** (149 tokens, stop: eos)

> He was so excited. It was a beautiful day. He wanted to go on the slide. He tried to reach it, but it was too heavy. He got a bit drops and he fell down. He was scared. His mom heard him cry and told him to be careful. She said, "I'm sorry, mom. I was wrong. I should have listened to me." mum smiled and said, "it's okay, you can't do it again. And you can't play with it." ben smiled and said, "thank you, mom. I'm sorry I didn't mean to break the candy again." his mom smiled and said, "of course, ben. You are a good friend."

**temp_0.5, seed 4** (88 tokens, stop: eos)

> He was so excited! He ran inside and looked around. He saw a big, tall tree. He was curious and wanted to have it. He ran around the lake and found a big, round balloon. It was so pretty, he wanted to take it home. He thought it was a fun day. He ran around the field and watched the birds. It was so much fun! He was so happy to have a new friend.

**temp_0.8, seed 0** (143 tokens, stop: eos)

> He was so excited. His mommy told him he needed to make it more treasures, so he took the diary home. Bob's mom tried to move the jet away, but it was too late. It was not wide, but it couldn't break. John cried and shook his head. He was scared that he could get very upset. Then, an old man came outside to get a big box. He told his mom what he had seen; he was so old. The old man smiled and said he must be a little girl. He was so mad! The man was very upset and missed the man before taking his pan. He was so happy to see his new sister and have a lot of fun.

**temp_0.8, seed 1** (112 tokens, stop: eos)

> It was so big and shiny. He wondered what it was. It was a big box filled with colors. He wanted to talk to the world. He looked around and saw a surprise. It was shiny and gray. He was very angry. He wanted to make it better, but he was scared. His mom told him that he had to leave the shop with his friends. They cleaned the room, put the pieces on the table. From that day on, tom made sure to stay in the same and watch his mom and dad for a long time.

**temp_0.8, seed 2** (129 tokens, stop: eos)

> He looked around and saw a big yellow boy. He had never seen anything like it before. He wanted to help the pigeon, so he picked up the scissors and put it in his mouth. He asked his dad to help. The poor old man tried to put the chair back beside him and the man finished his cut. The little boy was so happy. He said, "this, my juice is very nice." the boy grabbed the block, and he put it in his pocket. He smiled and said, "thanks, little boy!" the little boy was so proud of his step. He played with his toys every day.

**temp_0.8, seed 3** (150 tokens, stop: max_len)

> He was so excited. It started to drip the highest. He watched it in the air. When he pulled it up, the house began to drift. Now it was bigger and bigger! It had two green avocado and ran to the top. He touched the mask, and smiled. But then, something happened. He heard a voice coming from the garden. It was the shark that he had never seen before. It was a big, furry mouse! It seemed to be woken and head around. He asked the dog why the dove was so nice. He said, "sorry, tom. It's still tired." the deer was surprised and scared. He wanted to improve the rabbit. So, he looked at the way and said, "

**temp_0.8, seed 4** (150 tokens, stop: max_len)

> Suddenly, he heard a loud roar. He looked up and saw a big, round tree. The butterfly was sparkling and a white grey shell. The water was heavy and he had to go home. He tugged it close and tried to open it, but he wouldn't. Suddenly, he heard a voice. He was scared, so he ran towards the hole. The otter was scared and started to cry. His mother came out from behind the tree and saw the bird had fallen away. "Stop!" said the voice. "It's very dangerous!" the bully felt scared sadly in pain. He thought about what he had been scared and then waved his tears. The head was scared and said, "oh no!" his dad came

**temp_1.0, seed 0** (150 tokens, stop: max_len)

> He was so happy. His mommy told him he needed to make him feel better, so he took the diary home and put it in a lung. As he sat, his rug appeared in the sky! He slowly looked around and found a big pot of spray ice - candles! He ran over and tried to start it and the ball really even the sky. Zip giggled and pose it was time to go home. Jay went outside and skipped in the garden. The old man said, "welcome, ben!" the brown man checked the shape. She helped its mum go back to the bathroom with a smile on his face. Soon, ben ate acorns really hard with his new sack and he jogged up to his cave to make it feel warm.

**temp_1.0, seed 1** (111 tokens, stop: eos)

> It was so big and round. Jane wondered what it was. It was a scarf that could get full. "See what what this is?" tim looked around and saw a surprise on the table. He was so happy and said, "where are we going, let's make sure we want to finish his so soft." suzy smiled and said, "yes, sam! I love the sunrise with the red white flowers." from that day on, suzy made sure to stay in her warm and watch her mom and dad for her food.

**temp_1.0, seed 2** (129 tokens, stop: eos)

> "Hello, mommy. He is my grandma. What is it?" she asked. "This looks really brilliant," mom said. "I can stay longer. Questions for you," he asked. The old man shook his head. "I'm here, but I think maybe use something special in the bin," replied pete. He brought his toy train to the mill, holding his bag very cooler. Mark showed him how to block, but he liked to get things off dinner. As he felt comfortable with his rope, he felt glad he would be able to come out soon. He ran and walked his bed every day.

**temp_1.0, seed 3** (150 tokens, stop: max_len)

> He was so itchy. It started to drip the highest at home. He couldn't draw. "I know this cord is the nightmare!" tom said. It was bigger than it! "This is just an oxygen. How about it?" he told his mom and dad that he had no number to do. They did not know what to fix. Finally, the bus was fixed. Mum had a big bag of plastic drawings. Tom wanted to climb the object and dream and think of a number of other lollipops would get for an. So they did it, and it looked like a fire, or tired. Thomas's dad was happy he was able to make her promise called the bank. So, the little teacher had proved something special.

**temp_1.0, seed 4** (150 tokens, stop: max_len)

> Suddenly the fire began to stop john and john looked around, his eyes arrived. Suddenly, he had an idea. It started to rain again and he started to shake the big spikes. The rain was even more powerful than before. "Hey I don't believe it!" jane said, panicking. "I love you too, so it won't get you really?" jill looked at all around. She cracked in amazement and tried to resist it. She grabbed a small bite and started running around she saw a bright light. It was to a different day rolling through the air and sadly in the sunlight. But then, she got into trouble and blew the starry down in the air. It was a mug! The winter monkey arriving all around the

**temp_1.2, seed 0** (88 tokens, stop: eos)

> Ben lay down and started his adventure. When he came back, he put his paw on the grass. It touched the ground and croaked, but then something heard him move quickly. It was a loud noise outside from wide, smaller light! He couldn't believe what it had! From bob was almost startled in warning. And nothing seemed really scary! Eventually, zip giggled and pose it silent. He was so thankful to be with it!

**temp_1.2, seed 1** (148 tokens, stop: eos)

> It bent down to see what it tasted. He grabbed some energy all mark at the top but then he stopped moving. And what somebody did! Alvin was so happy! The next morning, dad spent his food. He followed his waist and he found something jam at her box - books. Then he saw his owner so much this o not. He said "look henry, sam! I bet the sunrise is the best white pile of lemons and waves!" john was very interested onto the train with his feet. He wiggled and right around and around the tent for a journey. The created memories was getting sleepy and max wasn't allowed to play with out. He didn't notice and then thanked him, happy he had made a blueberry.

**temp_1.2, seed 2** (58 tokens, stop: eos)

> Stitch was so excited. He carefully jumped and around and played games in the water. He used anticipation and more his boots and raspberry drops. He wears some olives pennies. Questions for awhile, at the ground, painting and fun. Peepers poor doughyman screaming, feeling the warmth he walked beside.

**temp_1.2, seed 3** (109 tokens, stop: eos)

> Everywhere it started to be different in the world. Timmy was amazed. He couldn't draw on the hot words. This never the nightmare came when tom didn't find a rock. It looked super sunny and humble. He ran over to hand and locks it. Sam smiled and smiled. He had so much fun playing and playing with on his club with his friends. Every night it was a song. Jill and a group of friends he shared with the pool. Janey felt happy. And she had a wonderful day garden at sports, letting her.

**temp_1.2, seed 4** (150 tokens, stop: max_len)

> Suddenly the pill began to stop john and john looked about the spell. His mom turned the jingle on herself. Amy was a bit grey from the man standing in need. He removed it into its eyes even tugged it with both hands, until he was still free, then pressed inside. He ran as fast as he was getting alive, until he was able to feel the moon soon twinkling at all. He remembered what the old boy had added. However, soon enough, the oak pit was tilted from warmer and then shouted to freeze yet with to wash his turn rolling through the air in sadly in the wild line. Ben said goodbye and didn't forget to make the clumsy track! From that day on, he would catch them every day - no longer

**topk_10, seed 0** (138 tokens, stop: eos)

> He was so happy. His mommy told him he needed to make him feel better, so he took the box from the kitchen and took a bite. The man made a loud noise with him! He was so happy and he ran away. But when ben went home, the little penguin ran away and was very sad. He had made a new friend. The next day, joe went back to the park to play in the garden with his toys and his favorite things. He was no longer scared, but he still knew that it wasn't important. But soon, the rain was gone, and the water was gone. Jimmy tried again and, he knew he was going in his home!

**topk_10, seed 1** (147 tokens, stop: eos)

> It was so big and round. He wondered what it was. It looked at a bright rainbow in the sky. He wanted to get the treasure, but the sky was too heavy. He asked his mom, "what do you do?" the man smiled at her and said, "I'm not sure. But I have to be careful and not give it back." so his mom gave him a treat with a smile. Then he gave it a big hug and a hug with it. "This is my pleasure and I will give you the most food!" she said. The little boy was so proud of his work. From that day on, he made sure to keep them safe, happy with his own things.

**topk_10, seed 2** (85 tokens, stop: eos)

> "Hello, mommy." he said. He took a big bite of it. He picked it up and ran inside. He showed it to his mom. The little boy felt proud that his dad had a great time at the zoo and his mom. They hugged him and said, "thank you, mom." john was so happy to be able to play with his mommy. He was so excited to be there.

**topk_10, seed 3** (141 tokens, stop: eos)

> He was so excited. It started to move. The sun was shining and it seemed like he had ever seen before. He was scared of how hard he was, but he knew it was something. Suddenly, an angel appeared. The man asked, "can we take some of my toys?" his mother smiled and said, "no, it's just a little girl. That can be a little bit. It will be okay." the man was excited. He grabbed a big stick. He pulled the stick with the stick. The little boy felt happy, and he thanked him for being honest. From then on, the little boy was so proud to see that the world had been safe.

**topk_10, seed 4** (106 tokens, stop: eos)

> Suddenly the car began to rain. The truck stopped and the sky was getting darker. The truck had no friends and it started to rain again. They all laughed and shouted, "it is my best toy! It looks yummy!" the boy was so relieved, he had a lot of fun. But then he remembered he had an idea. He decided to be careful with his new toy. He knew that his mom would come to his mom and dad. They went back to playing in the sand and had a wonderful time.

**topk_40, seed 0** (150 tokens, stop: max_len)

> He was so happy. His mommy told him he needed to make him feel better, so he took the box from the ground and took a bite. As he sat, his mum appeared and said, "good job, mommy! Can you please help me and give it to me?" he was amazed by how he could read out how he ate. His mom said, "it's easy to be patient and don't lose it!" he was so excited. She said, "I will help you find the way back home." he smiled and wiped the big water off his hands. When the sun was ready, he gave it a special pat to make with his family and all the treats. They went to his garden and enjoyed the

**topk_40, seed 1** (112 tokens, stop: eos)

> It was so big and round. Jane wondered what it was. It was a big box but the key was very special and couldn't run very fast. The little girl wanted to make a picture so she ran to the tree and pushed it down. When she got home, she thought it was a terrible idea. So she put the bottle in her pocket and tried to get it down again. The next day the girl made a wish. From that day on, the little girl never got into her dress and she was always so excited to share her flute.

**topk_40, seed 2** (150 tokens, stop: max_len)

> "Hello, mommy. He is my grandma. What is it?" she asked. "This looks really cool," mom said. "I can stay here. I want to play at the piano." jill was excited. She asked if she wanted to play with her. But the store said it was too heavy. "No, ben, your toy are very fragile. It is mine. We can't go." but ben was disappointed. He liked to get things off. He looked around, and finally said, "let's put the wagon back on the sofa." he put the pot in his pocket every day. Then the little boy gave tim another spoon. He thanked him and gave him a hug. He was so

**topk_40, seed 3** (150 tokens, stop: max_len)

> He was so excited. It started to move. The sun was shining and it seemed like he had ever seen before. He was scared of how hard he opened it. Tom laughed and ran to the living room. He ran to the top of the hill and slid down and smiled. But then, his friend john was scared. He saw his big rock and asked, "what can do that?" tommy said, "it's so pretty. But it has a long coat and my mouth. It's not like it's yours." so they did it, and it looked like a toy, or a bit bitter. Joe was happy he was able to make her promise. The next day, jimmy and his teacher went on a hunt.

**topk_40, seed 4** (150 tokens, stop: max_len)

> Suddenly the floor began to rain. The floor looked very hot and cold. So, he went to the store and found a big blue dress. He was very happy. He decided to take it somewhere else. It was time to return home. The next day, the day heard his mom calling him. "What's wrong?" ben asked. "You had to wear something special and it won't be scared now," he said. The two friends went to the store and gave him some butter to make the cake. It was delicious. He used its new arms to make his favourite snowman. He thought it was so good. He made sure to take the rest and make sure it was even better. The next day, a nice old

**topp_0.9, seed 0** (150 tokens, stop: max_len)

> He was so happy. His mommy told him he needed to make him feel better, so he took the diary home and put it in a safe place. He made a tower and stepped out of the cupboard. He looked around and found a big pot of spray ice - cream! He ran to the kitchen and held it tight. "I'm the treasure, how I can?" her mum smiled and said, "I like it!" he beamed and the old bear sang out. Finally, ben opened the door and saw the rainbow shape. He stopped feeling so relaxed and ran around to enjoy the sack. But one day, his mom rewarded him from the gate and said it was okay. The cop said, "it's okay, jack

**topp_0.9, seed 1** (122 tokens, stop: eos)

> It was so big and round. Jane wondered what it was. It was a scarf that could get full. "See what what this is?" asked the little girl, "how?" so she ran to the tree and pushed it down. When she got home, she saw a hook. It was a beautiful flower. She put it in the oven and grabbed it. She twirled around the snow with the red white flowers. Then she continued to bake her joy. She felt so happy with her and she was so proud. The frog taught molly that she would come back and go back home again.

**topp_0.9, seed 2** (85 tokens, stop: eos)

> "Hello, mommy!" he said. He took a lick of the water and ran after the umbrella. His mouth started to shrink. He felt so proud of himself. Suddenly, it started to rain. The other baby had been allowed to go to the house. He walked over to the store, hoping to touch it. But when he started to cry, the boy gave him a big hug. He was relieved.

**topp_0.9, seed 3** (91 tokens, stop: eos)

> He was so excited. It started to drip the highest at home. He couldn't believe how much he could play. He was scared of how hard he was, but he knew it was wrong. Suddenly, an angel appeared. The sun could not turn or farther, and the dust was dirty. It was red and colourful. On a few moments, the bird felt peaceful. It had made a little kitten. It was the most most furry stuff!

**topp_0.9, seed 4** (150 tokens, stop: max_len)

> Suddenly, he heard a knock on the floor. The sun was a deaf, four canvas! Tommy was so curious that he could have it. He started to get closer and closer and found a large ladder in the air. He stepped closer and touched the garden, but it was stuck in a cold tree. He was excited, so he started to bounce down the slide. Soon, when it was time to go home, he tried to resist it but it was too hard. He was running by but he thought the water was fast. He tried to turn up the edge, but he still couldn't move. He said, "don't forget you. You need to take things not go to sleep." john was safe and stayed around the

**topk_40_rep1.2, seed 0** (71 tokens, stop: eos)

> Suddenly he saw a big pile of colorful water in the sunshine. He put his hands on the grass and put them underneath the ground. Now, it was a magical place for ben's house! After a bath, john was able to stay down through the forest for an adventure! From then on, they jogged in their home and had lots of fun.

**topk_40_rep1.2, seed 1** (150 tokens, stop: max_len)

> It was so big and round. Jane wondered what is inside his box. At last, amy saw a little boy. The girl had seen something bad! The man looked for him. He smiled so she ran to him with his toys and ran to the kitchen. Her dad said it was important. Jill grabbed his puppy with her arm. "Look, my loves!" sam shouted again. The man put the red bag on the ground and gave it to her daddy. He asked him, "can you watch my mom and dad?" her mommy thought for a moment and then said: "yes please!" sam took up her favorite book to say sorry - he needed to wear the perfect spot to have fun! He wanted to taste this

**topk_40_rep1.2, seed 2** (150 tokens, stop: max_len)

> "Hello, mommy!" he said. He took a big bite of water and ran after the little boy. As he got there, he noticed something strange! It was a giant that made him sad. The man was scared because they couldn't do it, so he walked over to the store. "Do you need help?" jim asked. His mum smiled and gave them some candy juice. She put it on their fingers and placed it around her foot. Soon, the man used it into pieces. When the little girl was finished, he started playing with the yellow apple. He put on his hat and his favourite shirt! When they returned home, his parents were able to stay safe, and gave timmy back to his mom and dad

**topk_40_rep1.2, seed 3** (150 tokens, stop: max_len)

> Everywhere it started to be different in the world. When they got back inside, he saw that a little boy had never seen the truck of his own place. It was bigger than it! One sunny day, anna and her puppy went to the zoo with their dad. And there was no fish for lunch. John was scared as he saw his friends walking by, playing on the swings, the slide and running around. He laughed and shouted with joy! But then when someone came and caught him. He asked his dog why the train was so nice they did it. He said he should help him, so they both climbed up the ladder and began walking towards it. Spot was amazed of his big bike. His mom had warned him to make sure

**topk_40_rep1.2, seed 4** (119 tokens, stop: eos)

> Suddenly the floor began to rain. The truck looked like a little boy. So, he went on an adventure and it started to rain again. The sun kept brightly, until there was no matter what happened. It flew into his pocket until there was his new place. It was no longer frustrated for him! He was excited to see it. He decided to try to balance it back from all around. With his friends for the picnic, the man's dad found them, ready to go sailing. She was so proud of herself and everyone's parents said sorry, but they loved their idea.

## P3_unusual_character (an unusual character)

**Opening (human-written):** There once was a little cat who could talk, but she only spoke when it was raining.

Prompt words outside the RNN/LSTM vocabulary (seen as `<unk>`): none

### Vanilla RNN

**greedy, seed 0** (150 tokens, stop: max_len)

> One day, she went to the park with her mom. She saw a big, red ball. She wanted to play with it, but she was too scared. She wanted to help her mom. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked

**greedy_rep1.2, seed 0** (34 tokens, stop: eos)

> One day, lily's mom asked her to help her find the toy car. They were very happy and excited to play with the ball. They played together every day.

**temp_0.5, seed 0** (63 tokens, stop: eos)

> One day, she went to the park to play. She saw a big, scary cat. The little girl was very excited and said, "hi, I'm so tired. You can't have you to get out of the forest!" the old man smiled and said, "thank you, mommy!"

**temp_0.5, seed 1** (86 tokens, stop: eos)

> The little girl was very happy and she was very excited. She had a special book that she loved to wear her special dress. One day, she went to the park with her mom and dad. She saw a big tree with a big red dress. She wanted to show it to her mommy. She put on her favorite dress and put it in the oven. She was very happy and thanked the man for the wonderful day.

**temp_0.5, seed 2** (150 tokens, stop: max_len)

> One day, she was playing in her room and accidentally knocked on a big rock. She picked it up and said, "I am a bit scared, but I don't know what to do." lily felt sad and angry. She wanted to play with the ball. She ran to the edge of the hill and saw a big box. She was very excited. She picked it up and showed it to her mom. She gave her a big hug and a smile. She said she was sorry for her. She said, "I want to write with you. You are my best friend." lila and ben thank you. They say, "thank you, mom. You are a good brother. We are sorry. We have to be

**temp_0.5, seed 3** (150 tokens, stop: max_len)

> One day, she saw a big tree with a big lock. She wanted to get closer. She tried to reach it, but it was too heavy. She got a bit scared and started to cry. Just then, her mom came to the kitchen and told her to be careful. Lily's mom gave her a kiss and said, "don't worry, lily. I will help you." lily and her mommy went to the park with her mom. They played with her toys and read books. They played together every day and played with her veil. They all loved the cookies and the pup, and they both enjoyed the delicious fruits together. From that day on, lily and her friends were so happy and thanked the lady for her. They

**temp_0.5, seed 4** (60 tokens, stop: eos)

> She was very happy. One day, she found a big box of a big cake with lots of paper. Lily was very happy and started to cry. She had a big smile and she had a lot of fun. She was so happy that she had to wait for the rest of her house.

**temp_0.8, seed 0** (145 tokens, stop: eos)

> One day, she went outside to play. She had been walking in the garden, but she still couldn't find it. Suddenly, a gust of wind blew in the air. It was a loud noise! She looked around and saw a big tree. The bird was very disappointed. She wanted to make something special. Then, she washed the tall box and told the present to get her hands. Her mom told her that it was important to be patient and keep her diary that was very scary. She was so happy and started to cry. She didn't know what to do, but she knew she could help her and wait for her. Amy was really happy with her new dress and couldn't wait to play outside.

**temp_0.8, seed 1** (121 tokens, stop: eos)

> The bear would often fly away and help. One day, the girl decided to make a new friend. She ran to the tree and saw a big red car. She wanted to catch it, so she ran to the tree and saw the star. She smiled at her and said, "I'm so grateful! So you are so happy. Let's sit inside." sam was so proud of his work and he made sure he was able to eat the carrot. He was so happy, he gave them a cookie and tasty treats. He was so happy that he had saved the peace of kindness.

**temp_0.8, seed 2** (150 tokens, stop: max_len)

> Every day, she would go to her grandma and wear the puppy in the water. One day, she found a hollow of pastel playing in the sky. She wanted to climb it, but it was too late. She was sad because she couldn't do it. She just walked to the playground and saw the poppy cut in the sky. Then she heard a voice coming from the nearby, she saw the bird. It was a bad cat and lily felt sad. She wanted to read a new adventure and asked, "what is it?" she asked. "Who's mommy," asked her mommy. She walked over to the tree and saw the little dad. She was wearing some of the ice and wanted to buy it. He was so

**temp_0.8, seed 3** (150 tokens, stop: max_len)

> One day, she saw a stranger. She liked the cookies and she wanted to build the top. She pulled up a cloth and started to laugh. She opened it up and put it on the ground. When she got to the same, she saw a rabbit in the sky. She knew she could use the red cushions, but it was too big. Lily asked her mommy if she could take a place to a group of friends. Sarah loved going to the park with her mum and dad. She couldn't wait to explore the world. So, they went to the store to buy some candy. They put some cream in the cup and sat down from the bookcase. Lily was called of her favorite soup. She wanted to wash her favorite treat.

**temp_0.8, seed 4** (103 tokens, stop: eos)

> She was so happy. She had a new friend about her family. One day, she went to the store and found a big blue dress. She was very happy. She said it was too hard to get it. But her mommy told her not to worry, but lily was excited to try her crayons. She was excited to try it. Lucy's mom had to wear her food when it was time to go home. She learned that sometimes it's important to take care of playing in the forest she knows.

**temp_1.0, seed 0** (85 tokens, stop: eos)

> One day, the way found a little girl in the sunshine. She asked her mom if they could keep it tomorrow. Amy asked her questions, "can I taste more mail if you see everything? You are not wide, it's very big." lily loved her safety. From that day on, she was very happy and learned that even though it is important to always listen to her and take her to help others.

**temp_1.0, seed 1** (41 tokens, stop: eos)

> The bear realized that she wanted to help. She grabbed some energy all all around the park but the key was boring. And she had completed the unique snack to get rid of the surprise for the fairy.

**temp_1.0, seed 2** (129 tokens, stop: eos)

> Every day, she would twirl in her room and wear the puppy in the water. One day, she found a hollow of pastel ornaments. She wanted it. The girl poked her best song to her side. She was so excited. She asked herself if she could have a little one. Mittens was so excited, he couldn't believe how to be big, but the boy gave them, she felt silly very upset. Lily was happy because she was okay. After playing with her crew, mittens noticed that her shadow said with a big smile on her face. The girl was so proud of herself, she ran away in his bed every day.

**temp_1.0, seed 3** (150 tokens, stop: max_len)

> One day, lily's mommy asked. She liked the cookies and she wanted to build the thief. She pulled up a cloth and gave her how to remain the marble slowly to himself. "It's so thrilling!" her mom smiled and said, "no, my dear did not know she could use your red cushions, but on no, it's just a worse. It can do that." tommy was sad and luckily he couldn't do it. The monster had a problem and the leaves couldn't breathe at it. He tried to grab the cushion away, and it looked like a fire, so he decided to pick it up. He was very careful and let was called the bank. So, the little teacher hopped over to the backyard

**temp_1.0, seed 4** (150 tokens, stop: max_len)

> She was so tired. She wanted to remind her about her spell. Her mom said, "yes, mommy. It's just a pretty mailman." the owner smiled and said "yes, I need to eat healthy time." she said, "yay, let. Inside!" he went to the store. He put the thread in the kitchen and closed the lid for food. As he walked, he tried to grab his wings back hands. He grabbed his backpack and said, "stop! Meow!" tim shouted softly. He played slowly, rolling through the grass and sadly in the wild line. He said goodbye and smiled. Finally, the hunter rang the boat from the tree. John used the powder to wipe him out around the

**temp_1.2, seed 0** (124 tokens, stop: eos)

> Suddenly, she heard someone found her hand. She knew she had to behave and brought her favorite snack. Millie touched the desk and croaked, but then something heard a loud sound. It was a loud noise who blew wide in the grass earlier. She flew closer and saw safety! She ran over and tried to start it and the ball started to jump. Daddy told the present what it did something useful, before pretty happens. It hurt slimy, but the monkey wouldn't try that it was a lot of fun neighbor. From that day on, red would count its family, keeping ones and wore some honey at before.

**temp_1.2, seed 1** (150 tokens, stop: max_len)

> The bear realized the animals wanted to help. He grabbed some energy all all at the park but the key was boring. And timmy had no rescue unique because the ink made the mess timmy destroyed the doctor. He wasn't happy to find his things to prepare anymore at her. Katie thought he was deaf. His owner so soft. He gave him a hug - five orange and smiled. His mom gave him a treat with her mom and thanked her for bringing the gifted fake head that it could be proud of them. He wiggled and left the port around the tent for a journey. The created memories was always happy for max. He got in a big blue map, brush his box and then thanked him, happy. His friend welcomed him for great,

**temp_1.2, seed 2** (129 tokens, stop: eos)

> Every day, daisy would raise her bags and make different noises, her ears on daisy. Every day she would set in the raspberry drops of paper and packages. One day, annabel decided to be four food for her to do. One day albert introduced a slice of milk for her work. Mittens was so excited, they laid stepped on the table started to get back. Jane agreed and stayed into juice. She drew a huge well in her garden block, feeling walking smile. Eventually many nights lived, and every time she did the exercises she found them. She would read for cheese, happy to step after. The end thank everyone every day.

**temp_1.2, seed 3** (150 tokens, stop: max_len)

> Everywhere connie started math, she started to slip. When her parents watched she could build back on the hot words, though never the nightmare again when she didn't find a rock anywhere. Her mommy told her just should worry. She went to the bench and told lily to be careful not first or boat. Lily made her doll very on a puppy with another makeup, but the boys was afraid of first. Tommy took it home luckily he couldn't do it. Janey felt scared. And then, he decided to play at catch them. He got frustrated they did silly, and sorry to tom back it, or tired because he was calmer again. He was sure to make her feel called of better. So, the little teacher hopped on the swings.

**temp_1.2, seed 4** (36 tokens, stop: eos)

> She was feeling very impatient. John and john looked about other his friends. They decided to hang on the handle and swim a rug and play. They all lived happily ever after.

**topk_10, seed 0** (133 tokens, stop: eos)

> One day, the little girl decided to go on an adventure. She put on her shoes and started to read a new toy. She was very enthusiastic to help. She went back to the house with her mom. She was happy when she saw the new book that she had seen a great day. From that night on, lily learned to be careful and listen to the people who always make mistakes. They also told her that they had to take a bath. The old lady said, "that's a very nice thing, but you should be careful when you need the bath." lily and ben played together, but they also had fun and shared their toys.

**topk_10, seed 1** (57 tokens, stop: eos)

> The little girl was very happy. She had an idea! He had a special idea that could make him feel better. The next day, timmy went to the park with his mom. They saw his friends and they were both very happy and happy. They all played together every day.

**topk_10, seed 2** (85 tokens, stop: eos)

> Every day, she would wake up her room and eat yummy food. One day, she went to the zoo with her mommy and dad. They saw some big trees, some leaves and a big, shiny dress. They put flour in the oven and then they put the pieces on the table and the bag in the oven. They put the ball back inside, and soon they would always remember how to do the same thing.

**topk_10, seed 3** (114 tokens, stop: eos)

> One day, lily's mommy asked her to take a bath to the zoo with the little girl. She asked them to go on a big tree. The cat didn't want to share her feelings. She didn't know what to do and asked her mommy if she could have her favorite toy to her. Lily asked her, "can we play with my makeup, I can't fix it." mommy said, "yes, I will make you feel better." lily was happy to hear the butterfly and smiled at her, "thank you for being honest."

**topk_10, seed 4** (79 tokens, stop: eos)

> She was so tired. She wanted to show her parents, but her mommy told her that it had been broken and it broke her. It was a big, scary bird. The bird was so happy. She thanked the man that her friends were very happy to have the fun day. They played with the toys and ate them together. From that day on, tim and the rabbit went home.

**topk_40, seed 0** (150 tokens, stop: max_len)

> One day, the mother found her little brother in the garden. She asked her mom if they could keep it. She asked her mommy, "can I help you, it won't see me. You are not a little brother. Now we can use the food to make it feel better." timmy was sad. He asked him, "you should be very naughty and don't worry, I'll help you." tim was sad, but he knew the old bear was gone. Finally, jack went outside to help his mommy. He didn't know why the big bird got mad and wanted to play with it and he started to cry. He cried and saw no one. He couldn't believe how much he had found it. The fox

**topk_40, seed 1** (133 tokens, stop: eos)

> The bear would often fly away in the morning. One day, she decided to make a new dress full of toys. And she had a lot of fun to play with the toy. After the doctor was gone, she said goodbye and showed her the toy back at her. She thanked them and gave her medicine a treat. She was very happy and said, "that's very nice!" the man put the pieces on the table and closed her eyes. Then she grabbed a big chair, and gave them a cookie. She was so happy and excited that she went back to the kitchen table, feeling happy knowing it wasn't allowed to play in any trouble.

**topk_40, seed 2** (150 tokens, stop: max_len)

> Every day, she would twirl in her room and run. One day, she went to the store and found lots of vegetables. She went to the kitchen and sat down on the swing. At her mom, lily and sally were in the kitchen. She saw a big red dress on a bench in the water. It was a big box with lots of colors and leaves. She wanted to explore the world around there. Her mom gave her a big rock and a smile on her knee. Mittens was sad and said, "mommy, I want to put on on it first." she asked, "where's my car?" emma asked, pointing at her. They went to their room. She said, "hello, little girl!"

**topk_40, seed 3** (150 tokens, stop: max_len)

> One day, lily's mommy asked. She hugged her and thanked her for finding such a good home. After a few minutes, jane came into the woods. It was a big, beautiful butterfly. Sue didn't know what to do and asked about her brother for helping and decided to play together again. Lily was so scared, but then, her mommy had a dream on her wrist. The girl was very sad and didn't know what to do. She felt bad and decided to help the bird. She said, "well, thank you for saving me." and lily looked at lily's hair and said, "thank you, lily. I'm proud of you! You are very good." the little girl smiled and said, "

**topk_40, seed 4** (150 tokens, stop: max_len)

> She was so tired. She wanted to show her parents, but her mommy told her that it had been broken and it started to rain again. The puppy kept crying, and that it was safe. Lily knew it was time to keep something special. At first, the girl heard no loud noises. It was a big, beautiful diamond. The boy decided to try to reach it, but it was stuck with a hole on top. She said it was time to take a bath. She asked the shopkeeper to borrow the puppy, so everyone asked her mom if she could go too she could play with it. But then, she got into trouble and she started to cry. She cried and cried. Mommy ran to the house and saw a nice lady

**topp_0.9, seed 0** (77 tokens, stop: eos)

> One day, the mother found her little brother in the garden. She asked her mom if they could keep it. She asked her mommy, "can I tell you more mail if you attach me with you?" lily was excited and couldn't wait to start her own chalk! From that day on, she was known and always made sure to keep an old box in the sun.

**topp_0.9, seed 1** (150 tokens, stop: max_len)

> The bear would often fly away in the morning. One day, she decided to make a soft mess. But her mommy and daddy said she was okay. The little girl wanted to help her dad so she ran to the tree and pushed her down the ladder. At her box, it noticed a butterfly with its feathers. It wanted to see a butterfly flying in the sky, but her mom told him that it was wrong to be a little girl who was curious. She explained that it was important to take things that was just like. The girl nodded and thought for a moment. She looked around, but she couldn't find it. She tried to stop her, but she kept digging until the sky was empty. She laughed and said, "this

**topp_0.9, seed 2** (121 tokens, stop: eos)

> Every day, she would twirl in her room and wear the puppy in the water. One day, she found a letter and decided to go to the beach. When she arrived at the forest, she saw a little bunny who had wings in a big pile. The giraffe was soft and white and seemed to touch the turkey. The little girl was so happy, she said, "this, she felt so very nice and proud. She grabbed the block to her crib and showed her a kiss. It was so beautiful! Molly said," you're welcome, timmy. You are welcome to bed. "

**topp_0.9, seed 3** (150 tokens, stop: max_len)

> One day, lily's mommy asked her to kneel. Her mom said she could build the orange water and make them more taller. When they got home, she got a toy to her mom. "Can you pick me with my phone and I'll make something special?" her mom replied, "I know we was scared. They are very big and round, but please say that can be bad and feel a messy thing," sarah said. Lily was excited to see what she could do. Her mommy said, "well, thank you for saving me." and lily looked at lily's car and said, "thank you, lily. I'm proud of you! You are very good." the little girl smiled and said, "

**topp_0.9, seed 4** (111 tokens, stop: eos)

> She was so tired. She wanted to show her parents, but her mommy told her that it had probably destroyed. It started to rain again and they started to get angry. She said, "that's a powerful crayon and that," lily said. "I don't know," said lily. "What's wrong?" anna asked. "You are my hero!" from that day on, lily always remembered to learn that she had taken her special to go home. She couldn't wait to share the subway with her friends and played.

**topk_40_rep1.2, seed 0** (33 tokens, stop: eos)

> One day, the mother found her and gave her a big hug. Lily felt happy that they had done something bad to want to be a part of the world.

**topk_40_rep1.2, seed 1** (130 tokens, stop: eos)

> The bear would often fly away in the morning and watch tv. All night at the park with daisy's friends were special and always had fun together. Tim looked around him for making many things to his house! She asked her mom if they needed to prepare out at her. She thought it sounded interesting. Anna saw so soft that she didn't want to give it back by herself! Later that day, lily's mommy gave the doctor some big cones and said "yes, that is amazing, honey! And I'm just like this rock and you can bring food anytime." lily felt so proud of herself for being responsible and not happy anymore.

**topk_40_rep1.2, seed 2** (150 tokens, stop: max_len)

> Every day, daisy would look at her grandma and run. One day, she went to the store with her mom in the park. Amy loved to play with the toys on her house that to stay close. Everywhere she got there's wardrobe over all a beautiful, green room who liked to use things. One night, lily saw a friendly cat named mittens. Mia looked around for them, she accidentally dropped the candle everywhere high as she had found up! Sarah couldn't believe her eyes she smiled! Max asked, "don't be good friends," said timmy. "Yes, this is my birthday. Let's go here to see a lot of ice cream to make you better.. Next time, don't worry. Then he can fix

**topk_40_rep1.2, seed 3** (49 tokens, stop: eos)

> One day, lily's mommy asked her to kneel. Her mom said she couldn't use the puzzle and how she had never been before for dinner. From now on a journey, everyone looked around and saw all the wonderful things in the sun.

**topk_40_rep1.2, seed 4** (51 tokens, stop: eos)

> One day, lily's mommy suggested the doctor and said, "let's go over the hill to finish it together!" but mary thought it would be cool. Mom said that it was safe because her sister couldn't play with her instead of mittens.

### LSTM

**greedy, seed 0** (150 tokens, stop: max_len)

> One day, the girl was playing in the garden when she saw a big, scary cat. The cat was scared and wanted to help. The cat wanted to help the cat, so she ran to the cat and said, "I'm sorry, I'm sorry. I will help you." the cat was very sad and said, "I'm sorry, I'm sorry. I will help you." the cat was very happy and said, "thank you, little girl. I'm glad you're safe." the little girl was so happy and thanked the cat. She said, "thank you, little girl. You are a good friend." the little girl was so happy and thanked the cat. She said, "thank

**greedy_rep1.2, seed 0** (115 tokens, stop: eos)

> One day, the girl wanted to make a new friend. She asked her mom if they could go on an adventure and play with her friends. The girl said yes, so she went to the park to play. She saw lots of animals playing in the sky and had fun. She was very happy and excited to explore the world. She ran around the forest and watched as the sun began to set. She felt like she was flying by. The girl was so happy that she forgot about the big tree. She knew she would always remember the day she found something special.

**temp_0.5, seed 0** (132 tokens, stop: eos)

> One day, the little girl decided to go for a walk in the park. She saw a big tree with a big tree. She was very excited to tell the bird to go home. She asked her mom if she could take the bird to the bird. The bird said yes and she was so excited to see the bird. So, the bird flew up high in the sky and the bird flew away. The bird flew around the garden, and the bird was very happy. The bird flew away and the bird was happy to have a friend. The bird was so happy to have a new friend. The bird was happy to have made a new friend.

**temp_0.5, seed 1** (128 tokens, stop: eos)

> The girl was very happy. One day, she saw a big, scary cat outside the window. The cat wanted to play with the cat, but the cat was too strong. The cat was so sad and scared. The cat wanted to help the bird. So, the cat climbed down the tree and grabbed the bird. The cat was very sad and flew away. The cat was sad. The cat was hurt. The cat tried to catch the cat, but it was too late. The bird was too scared to come back. The cat was too sad. The cat was sad. The cat was sad. It was still alone.

**temp_0.5, seed 2** (113 tokens, stop: eos)

> One day, she was playing in her room when she saw a big, scary bird. The girl was sad because she was scared of the dog's cat. The cat wanted to help the cat, so she asked her mom to help her. The little girl put the cat in the cage and took it away. The cat was so happy to be free. The cat was very happy, she felt like she was flying. The cat was so happy to have a new friend. From that day on, the little girl was always careful when she saw the lizard.

**temp_0.5, seed 3** (150 tokens, stop: max_len)

> One day, the cat saw a big, scary cat. The cat wanted to help the cat. The cat was sad and started to cry. The cat meowed and said, "I'm sorry, I just wanted to play with you." the cat was very sad and did not know what to do. Then, a little mouse came to the rescue. The dog said, "I am sorry, cat. I am sorry I couldn't play with you. I will help you." the cat smiled and said, "I'll help you." the cat and the cat played together until the sun stopped. The cat and the cat played together every day. The cat was happy and safe. From that day on, the cat and the

**temp_0.5, seed 4** (96 tokens, stop: eos)

> She was very tired. One day, she found a big box of mud. She wanted to try it. But it was too hard for her. The girl tried to fix the box, but the cat was too close. The girl was sad, but she knew she had to do something else. She decided to take a nap. She started to play with the red ball and the cat. She liked to make people happy. She was so happy. She was very happy.

**temp_0.8, seed 0** (150 tokens, stop: max_len)

> One day, the little girl decided to sneak in the sunshine. She put on her shoes and started to walk in the grass. She was very excited to tell the bird to go home. She closed her eyes and looked around. When she arrived, she saw a bird flying in the sky. The girl was so excited and stopped to explore the garden. She told the bird to look for something to explore. The bird flew around the night, and around the grass. She sang a song and had a lot of fun. When the sun went down, the worm flew away from the lake and the grass went down. And she sang songs and ate acorns with joy. She played it every day and thanked the bird for help. She waved goodbye to

**temp_0.8, seed 1** (107 tokens, stop: eos)

> The bunny would laugh and sing. One day, the bird stopped all all about a sudden. The rat was very scared and couldn't run away. The cat was very sad and started to cry. The cat tried to help the cat and get the bird back at her. She thought it was very bossy and decided to use this cell. The cat said, "don't worry, I will help you with the red white bird." from that day on, the little bee never got into her cat and she was always worried.

**temp_0.8, seed 2** (116 tokens, stop: eos)

> One day, she was a bit stubborn and she wanted to find a toy. She looked out the window and saw a small, scary cat. The cat was scared of the little kitten, but she wanted to catch the baby. The poor cat was scared and didn't know what to do. The girl said, "I can help you." she took a deep breath and stopped, but she was very careful. She was so happy and she felt safe. The cat was determined to explore the day every day, with the cat's fur to put on her special pillow.

**temp_0.8, seed 3** (102 tokens, stop: eos)

> One day, the cat had a long idea. She wanted to succeed at the same thing. She tried to play more, but nothing could not fly or say it. She was very sad and didn't know what to do. The cat asked her if she was ok and decided to walk down the street. Her mommy and her mom started to ignore her. They felt bad and wished they could stay in the store. The moral of the story is that it's important to be careful and share with people.

**temp_0.8, seed 4** (83 tokens, stop: eos)

> She was sad because she should not find any food about her family. One day, the cat had an idea. She started to argue about the man's dress. The cat decided to invite her to need his powerful crayon and that she liked to speak at the flowers. She thought it was sweet and had fun. She was so happy and excited that she couldn't wait to play with her friends. The end.

**temp_1.0, seed 0** (140 tokens, stop: eos)

> One day, the little girl decided to sneak in the sunshine. She put on her glove, and went to a tree. She croaked, but then something heard a loud sound. It was a loud noise outside. Wide was alone and couldn't believe her eyes. She started to tremble in excitement. Startled, warning, and the ball started to shake. The zip giggled and pose it lifted the wall. The girl saw a pond with white air and a small eye. She sang out of a rock in her neighbor's brown body. The kitten sang up and then flew away from the lake to enjoy the rest of the day she found back into amy's house. Liz never played it too much!

**temp_1.0, seed 1** (114 tokens, stop: eos)

> The bunny would laugh and sing. One day, the bird stopped all becoming a little bit but then she stopped playing. The next day, the unique bird looked at the herbs and smelled a princess so she couldn't help appear. Finally, the bird showed her how to twist the rock. Then, the caterpillar flew so soft that she noticed that the lamb had become orange and liked her porridge. The little girl was very happy to have a big friend. The gifted fake flower was so happy, proud of her special cookie she could go outside and play with her paw.

**temp_1.0, seed 2** (150 tokens, stop: max_len)

> Every day, she would raise her arms and make different noises. Her friends stood and played together every day. They walked and laughed, stretching and having fun. The girl was so proud that daisy had drawn a great time at school. Poor day, a little girl loved to dance. She watched the flower flutter, cut it, and even then started to fly high. Jane would run, jump and twirl around. Everywhere she went, she would block to her friends smile. Eventually many kids lived in the sun, and with all kinds of singing, hearts and blueberries. She could learn to learn how to dance, and thank everyone every day. One day, dad saw a modern cactus. It saw some books in a puddle. Then he remembered how

**temp_1.0, seed 3** (51 tokens, stop: eos)

> One day, the cat had been searching so much. Her parents watched him and smiled back. "I know this is never unusual," the turkey replied. It slowly put himself under a chair and said, "yes, I will love us!"

**temp_1.0, seed 4** (150 tokens, stop: max_len)

> She was sad as she danced, and she looked about her spell. One night, the cat had an idea. It started to rain again and the sun kept on the floor. It was too strong for everyone to do anymore. "This is not hidden to work. That is no one to leave it around." she wanted to find something that would be really bad. She looked at all her toys and said, "don't worry, it's okay. I had never seen a cherry pastel warmer." the girl smiled and said to the bear, "we're feeling bowing sadly in my wild box. I can find something new. I will make you happy with being so big and smart. I love jumping by monkey arriving if you want

**temp_1.2, seed 0** (150 tokens, stop: max_len)

> Then one day the way found a cop when she came for a while. Then, ava remembered that the diary was had a new picture of a small worm! The curious dog was very happy! Lila wanted to feed wide, but the microphone was fierce. The bird told the little penguin bob that if they fly in the earth and so, the daughter worked hard with the present pose. So, the yacht swam away slowly when they cleaned up in a lazy adventure. Kitty carefully sang out all a lot of fun sunny of the interesting apples. She sang up if she could play with the water and enjoy the sack before she played out of the yard. Acorns woke up with her small sack and janey jogged down front of the slide and waved goodbye as she

**temp_1.2, seed 1** (150 tokens, stop: max_len)

> The swan seemed to fly away. Jane tried stories, but still all she couldn't figure but then she stopped clapping. The chickens had fallen very unique because the flower made the sheep feel bad. So there food and two appear on its eyes and the pepper allowed to be safe soon. After a week, anna saw so soft that she noticed that there had broken sauce. Mrs. Doggy cleaned the rose from people and forgot when the dancers scurried away. Then leo waved goodbye to that it was gone with learning and she was just like right before and her frustration was safe. Mom smiled and created how she was happy to have her dreams of her smart birthday to say sorry - for it and then thanked her friends again. Leo loved welcomed the new taste,

**temp_1.2, seed 2** (150 tokens, stop: max_len)

> Stitch was happy to have a license one and he added a puppy in the water. She carried the umbrella back in the sea and turned under a branch. She sat down on the best speed to loosen her hands. As she waved back poor day, a tired sunset spotted a soft web. The pen said goodbye, cut it through a thick tree started to fly back. Jane gave the little flower juice and would get it high. She grabbed the block, and filled it with her crew. Mittens settled into her buckets, with water and happiness singing to put her on. She flew right out of step and ran towards it. Everyone every day, they all spread dad to make another circle. The raven had a delicious string with saved vinegar in her yard

**temp_1.2, seed 3** (150 tokens, stop: max_len)

> One day, the cat had been searching so much. Her parents watched at the same thing. They tried words but never never resisted again again when they didn't find a bigger favorite way to succeed. Suddenly, an angel appeared. The cat asked about how fast she found and decided to walk down the street. So, they went on a puppy with another makeup, playing on the wall, until they arrived at a group of friends he saw with scratches lines. Janey felt happy. She felt so lonely that she splattered at the same branch. Tom read veil to all the places he looked like none happening, or stopped playing. The deer was happy he was sure to make her promise called the bank. So animals played gather together every morning. This time

**temp_1.2, seed 4** (150 tokens, stop: max_len)

> She was sad as she danced, faster from a deep evil spell. One night, the cat had an idea. It a rug and started to fold the paints. The cat removed it into its fur even more powerful crayon anymore. "This most very soft,'I blink. Inside are balancing sweet germs" "love, bun, hands," amy exclaimed. The animals were both impressed when all the queen who came in her book, added the hands. Soon she arrived, crying and was so happy she went to the woods. Before everyone to wash her turn, the edge of she sadly in the wild line, ready to find something new. Finally, the starry bird shined its head up and mr. Mug smiled and wrote out arriving - lucy was

**topk_10, seed 0** (133 tokens, stop: eos)

> One day, the little girl decided to go in the garden. She put on her shoes, and went to a tree. She saw a pretty tree with flowers in the sky. It was so big! She wanted to see it up. But when she reached the bird's window, she saw her mother in a hole and asked her what was wrong. The girl explained that it was a very special place to help her. They decided to take a closer look, but she was too fast. She started to feel sad and sad. The little girl didn't think about the bird's feelings and wanted to be her friend and she wanted to be a new friend.

**topk_10, seed 1** (150 tokens, stop: max_len)

> The bird did not care. It did not know where the bird had been so much and could not be friends. She wanted to find the bird, so the girl decided to give out a picture of her friends. She thought it was so pretty. The cat asked her how she wanted to eat. The lady said yes, so she put the dress down. She was very happy and ate the delicious treats with the girl. The girl thanked her friend for the day and the girl felt happy with her warm toy. She made sure to make her own music with her friends. She learned a lesson: always be kind to others and not make things happy to help others. She was proud of her new friends and always remembered how to play with her friends

**topk_10, seed 2** (150 tokens, stop: max_len)

> Every day, she would wake up her room and make a big mess. She liked to explore the forest and make them happy. One day, the cat saw a big tree with a big smile on her face. She was very excited to see all the other animals, but her mom said she could help the birds who was safe. The cat felt sad, but she didn't understand how she wanted to be. Her friend said, "hi, bird! What do you get?" the bird smiled and said, "yes, I want to see you!" the little mouse was happy, and they played together all day long. When they were done, they both went home. The girl had a great time with her family in her garden

**topk_10, seed 3** (150 tokens, stop: max_len)

> One day, the cat had been going so much. Her parents came over and saw the cat. She was very excited to play with her friends. The cat asked a dog if it was okay. Sue was so excited to play with the cat. She went for a walk in the forest and saw a small cat. It was so big, with its tail, fluffy, fluffy. The bird wanted to try a cat, so he ran away. But as the bird was about to help the cat, she saw her friend, a little girl named mia. Tom wanted to play with tom and lily, so they decided to help. They both looked around and saw a little bird in the garden. Sue was very happy and wanted to play. But

**topk_10, seed 4** (104 tokens, stop: eos)

> She was sad because she couldn't find any food or other things. One day, the cat had an idea. It said, "I want a big dress. I'm going to find my favorite toy. It looks yummy." the cat was very excited and started to dance. She ran as fast as she was flying, so she started eating, feeling very happy. She danced around all around her with the bird, and she was so happy. She was very happy to be able to be safe and happy.

**topk_40, seed 0** (150 tokens, stop: max_len)

> One day, the little girl decided to go in the sunshine. She put on her shoes, and went to a tree. She saw a pretty tree with flowers in the sky. It was so loud! She jumped and started to pick the cat through the forest. She had lots of fun playing with the other animals. And the ball was very tall. The lizard loved the sun and the sky. They loved the music and had fun. But then, the kitty slipped onto the ground. A strong monster came by. The girl saw the kitten. She stopped its head. She ran away to pick up the bird. And she soon wanted to explore it. The mouse tried to fix it with its wings. Amy went to find more food. She

**topk_40, seed 1** (143 tokens, stop: eos)

> The bunny would laugh and sing. One day, the bird stopped all all about its fun. The rat was very sad and couldn't run away. The cat felt guilty for making a poor mess so she couldn't help her. Finally, the bird showed her how to take a nap. Then, the panda saw so soft that he had a bit hurt. He tried to give her his medicine to put with the red ball back and the bird wouldn't taste anymore. The bird felt better, and he decided to go back and play with it. The dragon smiled and then came back up to visit him. He was very glad of the new book to say sorry to his friends and that they were friends again.

**topk_40, seed 2** (150 tokens, stop: max_len)

> Every day, she would raise her arms and make noise. One day, she spotted a small thing on the ground in the corner of a nearby tree. She wanted to climb it, but it had caught a little bit of her wings. She climbed a chair, and slowly walked to the playground. But the little girl was too scared. Then she heard a voice coming from the tree, she saw the kitten. It was a kind cat and she said "what do you get here?" the bird asked, "don't be scared, I want to make it come back tomorrow." the bird was so happy to be free! When they found the bird, they took a soft and warm wing and gave it back to polly. She was

**topk_40, seed 3** (100 tokens, stop: eos)

> One day, the cat had been searching so much. Her parents watched him and smiled back. "I know this is a new house, when you're so strong!" the kitten said. "I just am so tired." she asked about her words for her and decided to play together. So, she was scared of the bunny, and soon she fell asleep on the wall. The girl was very sad and didn't know why. Finally, the girl felt better. She felt helpless.

**topk_40, seed 4** (150 tokens, stop: max_len)

> She was sad as she waited for the little girl about her day. One day, the cat had an idea. It started to rain again and the sun kept on the floor. It was too strong for everyone to do anymore. "This is not fun to have fun. You'll want to leave it around." she looked at the puppy and thought about it to be brave. When it was time to go home, she tried to resist the dog. She was scared, and she couldn't believe her eyes. She ran out with her paw slowly, and couldn't give up. In the end, the cat heard all of the animals and she started to cry. She cried and looked up at her other dog. The dog saw lucy struggling

**topp_0.9, seed 0** (150 tokens, stop: max_len)

> One day, the little girl decided to sneak in the sunshine. She put on her glove, and went to a tree. She saw a bug with a big lemon, a rug, and a loud cat. She wanted to take the walk away. "Where bird is the fence?" she asked. The bird replied, "I'm hungry, I want to tell the bird." the angel said, "don't worry, I will help you." the bear said, "yes, you can have some of them." the rabbit smiled and then flew away from the lake to enjoy the rest. She was so happy and grateful. She played and played with the sack and played with the pink pink fish. And she lived happily ever

**topp_0.9, seed 1** (147 tokens, stop: eos)

> The bunny would laugh and sing. One day, the bird stopped all all about its song. The rat was fascinated. The bunny had seen a unique party with many animals, so many people in the tree! She worked with the flap of the bird and smiled at her. She thought it was very successful and could talk to animals. The red girl had so much fun exploring. She twirled along the grass with the red white flowers and the animals. Then the little girl forgot that it was time to go home. She gave the bird a big smile and told her they had a great time together. They waved goodbye to her and got off a big blue tree. They decided to come back and tell everyone about it for the prince.

**topp_0.9, seed 2** (150 tokens, stop: max_len)

> Every day, she would raise her arms and make noise. One day, she spotted a razor in the garden. She was excited, so she decided to stay inside. But when she got to the ground, she saw a big tree with a big, sharp feather on it. The cat was curious, so she ran to the house and opened it. Inside, she found a toy, she had never seen such a high sun. It was big, blue, and yummy. The girl smiled and waved her arms in her arms. It was so strong and long. She flew over to the clouds and started to eat it. Every day, she found a book of peace and makes some memories. She loved to catch her friends and have fun together

**topp_0.9, seed 3** (150 tokens, stop: max_len)

> One day, the cat had a long idea. She wanted to succeed at first but she kept having hot words. She would dream of her when she looked so strong. After a few weeks, the two purple were so tired. The cat taught kitty how to fly, and did not know how to use the red cloth. Then the crane started to fix its tail. The cat was so excited. It jumped down and pressed it down. It got very far away. The girl and her cat played until they were at home, making her faces for saving each other. And it was just easy to scare her. Then the cat would fly to the store with her friends. She was so happy and excited. She had become happy and gave the puppy

**topp_0.9, seed 4** (150 tokens, stop: max_len)

> She was sad because she should not pick up a cat. One day, she decided to talk to her friends. She started to argue about the man and the owner. The cat and the dog became friends. The queen and her friends liked to share. They shared the apples and played with the dog. The puppy was excited to meet a new friend, a friend named sue. Sue wanted to climb on a boat, but she didn't want to pick. She said, "mom, I am safe." sue said, "but I'm careful I think we can give you a treat." sue thought about what tom had to help and play. She had a great idea. She said, "good dog, mrs. If you want

**topk_40_rep1.2, seed 0** (124 tokens, stop: eos)

> One day, the mother found her little brother in the garden. He asked his mom if they could keep it. Her mom said yes, so she took a nap with a smile on him. After a while, she was now ready to get back home and play outside. As she skipped around the field in a deep slide and the clouds finally stopped. She told the people what it did and she gave him a hug. Then he went back home and showed the old lady that was very cool. She said "where do you go?" her dad nodded its head, and ran away to enjoy the beautiful treat.

**topk_40_rep1.2, seed 1** (122 tokens, stop: eos)

> The bunny would laugh and sing songs to her stories. One day, all of its friends were very adventurous. They did not talk to each other and played with their toys for them. After playing - there was a big tree on its way. The bird said hello, but she thought it sounded fun. So, so she put some water in her mouth. She gently folded it carefully again. The dove put the red veil in the air and ate it by her. The bee felt better, proud that sometimes she was just like right before and she learned that sometimes people use things if you be safe again.

**topk_40_rep1.2, seed 2** (129 tokens, stop: eos)

> Every day, the girl would go to her backyard and played with her friends on. One day, while they were in the park, amy found an unusual yellow apple. She wanted to play at the tree, so she put the key in a big pile of string into a soft place. As she picked it up, she saw a friendly cat! She asked them if she gave them, she had helped someone get some bread. She grabbed two pieces, ate a bird and tied it off the table into her bed. With the feather, the bunny put the worm back on. She loved to splash in the leaves in his garden every day.

**topk_40_rep1.2, seed 3** (109 tokens, stop: eos)

> One day, the cat had been searching so much. Her parents watched him and smiled back. "I know this is here to go!" tom didn't find a toy. So he reached a soft box. The cat followed the cat's hand and went inside. As she walked in she saw something new at playing, it was very high with its paw. She wanted it that day that she had tried a key from the dog. With a smile, the bird started eating and its cat felt proud of herself at home, for her.

**topk_40_rep1.2, seed 4** (150 tokens, stop: max_len)

> One day, lily felt better when the doctor noticed the sun shining her. She decided to try on herself when it was a perfect place from the pool. After a while, the girl found its best toy in it. She gave her a big hug and said, "look inside! What is this?" the lady replied, "yes, that's my friend? I want food too. I will never see now again soon, so you have to find something to go here." the panda smiled and then went to sleep. Everyone's mom said, "we're always ready for you to bathe now." the little girl didn't think about the answer. She loved spending time every day together, but the old lady would help people with

## P3_problem (a problem that needs solving)

**Opening (human-written):** The bridge to the town broke in the storm, and the children could not get to school. Lily had an idea.

Prompt words outside the RNN/LSTM vocabulary (seen as `<unk>`): none

### Vanilla RNN

**greedy, seed 0** (150 tokens, stop: max_len)

> She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she could go to the park. She asked her mom if she

**greedy_rep1.2, seed 0** (89 tokens, stop: eos)

> She asked her mom if they could go on a trip. So, she went to the store with her mommy. When she got there, she saw that it was very hot outside. She looked around and saw a big tree. She wanted to see what was inside. But then, something strange happened. The little girl was sad because she couldn't find any more anymore. She knew that she would always be careful and listen to her friends.

**temp_0.5, seed 0** (150 tokens, stop: max_len)

> She asked her mom if she could go to the park. She asked her mom, "what's wrong?" her mom asked, "I'm sorry, lily. I was sorry. I'm sorry, lily. I didn't mean to break my toy car." lily was sad because she couldn't do it anymore. So, she went to the kitchen and asked her mom what was wrong. She told her that it was important to be patient and not to get the ball. Lily was sad because she was very sad. She wanted to play with her friends, but she didn't want to share her toys. She asked her mom, "what are you doing?" she asked. "I'm going to make a cake!"

**temp_0.5, seed 1** (76 tokens, stop: eos)

> She wanted to make sure it was a special place. She was so excited to see the pretty flowers. She ran to the tree and saw a big tree. She looked for a long time, so she ran to the tree and saw the big tree. She was so happy she couldn't believe it. She was so happy that she had found a special surprise for her family.

**temp_0.5, seed 2** (87 tokens, stop: eos)

> She asked her mommy if she could play with it. She was so excited! She ran after the little girl and walked up to her house. When she got to the top, she saw a big tree. She was so excited. She asked her mom, "can you help me find a new flower?" lily replied, "yes, I can help you." she smiled, she felt proud of herself for helping her.

**temp_0.5, seed 3** (34 tokens, stop: eos)

> She asked her mom for help. But her mommy said no. She said they could draw on the table and play with her toys. They played together and had fun.

**temp_0.5, seed 4** (55 tokens, stop: eos)

> She wanted to succeed. She asked her mom if she could go to the theater. She went to the store and bought a big box. She put the key on the floor and it was very hot. She was very happy that she could help her mommy to play with.

**temp_0.8, seed 0** (25 tokens, stop: eos)

> She lay down and started to go back. She had been walking by one side, but she still couldn't find it!

**temp_0.8, seed 1** (118 tokens, stop: eos)

> She bent down to see what it was. She grabbed some energy all the leaves and the two of them was very special and couldn't wait to play with the puzzle. The next morning, the doctor heard a big noise appear on the ground. The bird said hello, "can we get a closer look?" so, this time, the barn had an idea. He decided to take the first walk with the red ball. He held it tightly and held it in his hand. He had never seen this before he just like it before and it was safe for him. The end.

**temp_0.8, seed 2** (43 tokens, stop: eos)

> She asked her mommy if she could know her paper and said, "mommy, can I give this pan?" she asked. Mama said, "yes, I want to make you happy to be safe."

**temp_0.8, seed 3** (150 tokens, stop: max_len)

> She wanted to know what it was. So she asked her mom, "what's back on?" the girl asked her mommy, "how does I say it?" her mom asked, "can I pick it with me?" asked lily. "Lily, and did not know what to do?" mommy asked. On a few minutes, lily's mom said it was a stranger. Lily's mommy said, "I want to be careful. It is easy. And I can't find it." mary thought for a moment for they to put the quiz into the village. It was still tired because it was too hot to use the lock to make her feel better. She saw that her journal was scared and lily said, "

**temp_0.8, seed 4** (150 tokens, stop: max_len)

> She wanted to succeed. She asked her mom if she could go. Her mom said yes, but they didn't want a rug. Lily didn't know what to do. She said, "that's a powerful idea anymore." she said, "don't worry. I'll send you to the hedge." lily felt so happy that she decided to try to show her mom when she saw her mom on the stage. Lily smiled and said, "thank you, oak. You are very brave and smart. Your dear and everyone's very careful." the little girl welcomed sadly in the wild box and gave her a hug. From that day on, lily always tried to tell her to always be careful with her friends and kiss her requests

**temp_1.0, seed 0** (103 tokens, stop: eos)

> She lay down and started walking in the water. She didn't want to stop playing with her balloon. But no one didn't go. Molly felt very sad and curious, so they decided to share some cookies. Lily was happy when she put on her envelope and started to rub the pieces of her mother's warning. Then lily's mop was the best bracelet ever. Johnny was so happy and she gave him a hug. They continued to take a bath and the old bear said goodbye to a lot of fun.

**temp_1.0, seed 1** (101 tokens, stop: eos)

> She bent down to see what it was. She grabbed some energy all all around the park but then she saw something special and she had seen a unique party. She looked for a surprise, hoping so she couldn't see what was inside and get the key back at her. She thought it was very interesting and could so soft. She put the snowball down in the orange and enjoyed her delicious clean clothes. She played with her mom and thanked her for helping the gifted fake show that it was gone forever.

**temp_1.0, seed 2** (67 tokens, stop: eos)

> She asked her mommy if she could know her paper and said, "mommy, can I give this pan?" she asked. Mama went to the sheep. She hugged her for her mom to her. Lily felt very happy. She was excited to do it, and he couldn't wait to see it again. He was happy.

**temp_1.0, seed 3** (150 tokens, stop: max_len)

> She was walking up. She started to slip. The sun was hot and they both had kept home, making a whole noise. They worked together every day and it made everyone happy. "Wow, two purple avocado!" they went to the zoo and bought the watch and decided to walk down the path. John was scared, but he trusted his friend. He felt bad for saving him that he had gone. He picked it up and carried it to the center. The girl and her cat played together in the garden when they found the treasure for they to enjoy the safari. The village was so happy to have some juice and candy was happy to hear them. Jane was happy that the lady had to do a walk together! Lily said, "

**temp_1.0, seed 4** (44 tokens, stop: eos)

> She wanted to succeed. She asked the doctor why about her spell her toy, she thought it had herself. Lily was a bit scared again and they started walking. The next time, they had finished even more powerful.

**temp_1.2, seed 0** (150 tokens, stop: max_len)

> She lay down and started walking in the water between her hand. However one day, ava showed buddy to a shooting tree! Ella croaked, sitting on the flowers and jumped in. Lily's mommy saw how fantastic she looked in the planet after dinner. "Wow, that's!" bob said excitedly. Max held back and smiled out, then the monkey took the curl present pose. So, billy played with the game games and he shared them; he was ready to try that time was a while in the sunny place and forever. The boy sang up and its family hugged him off. Dotty was upset again before taking his pan with his friends. Acorns woke up with her small sack and licks the boat tightly. After they finished, she hugged back

**temp_1.2, seed 1** (150 tokens, stop: max_len)

> She bent down to see what it belonged. She grabbed some energy all ear at the side but then she stopped working. And she had seen something unique! The little girl wanted to surprise daisy and so she ran by herself with dirt. When he arrived at the hole, she saw many people and birds underneath the flowers so soft. Izzy noticed that there had so much fun exploring. She twirled along the tree with the red white flowers and some circles. Then she was fake very beautiful. With this toy, and she was so happy. She liked her writing that she lead. She jumped up and looked at it for max. As she walked for a walk, she saw something appear and strange grass by her mommy. She asked welcomed rabbit to taste her

**temp_1.2, seed 2** (52 tokens, stop: eos)

> "Goodbye, mommy. Let's play hide and seek. We need to be daisy. If we follow your neighbor in the blanket instead?" from sheep. Tim hugged questions for best that to stay close to life and always talk back to his special friend.

**temp_1.2, seed 3** (150 tokens, stop: max_len)

> She was walking up when she saw a penguin that. Her parents watched him in the garage. "I know this though never dream of the honey!" so, lily put himself with her thumb and started her pick away. Bella went to the bench and told lily to be careful not first or boat. Lily made her doll very on a puppy with another makeup, but the boys was afraid of first. Tommy took it home luckily he couldn't do it. Janey felt scared. And then, he decided to play at catch them. He got frustrated they did silly, and sorry to tom back it, or tired because he was calmer again. He was sure to make her feel called of better. So, the little teacher hopped on the swings.

**temp_1.2, seed 4** (22 tokens, stop: eos)

> She wanted to succeed. Her mom smiled kindly and said, "yeah, you will make wonderful staff."

**topk_10, seed 0** (95 tokens, stop: eos)

> She asked her mom for help, but she was also very sad. But then, her mommy took her to a big, heavy blanket. Lily was very excited to play in the park. She asked her mom to go, but when she got there, she saw that the little girl was very sad. She was very sad and cried. She wanted to play with the cat anymore. So, she gave her a hug and they continued to explore the garden. The end.

**topk_10, seed 1** (150 tokens, stop: max_len)

> She wanted to make sure it was too late. She started walking, but she couldn't find the key. She started to cry and she was scared because the little girl wanted to help her. So she ran to the tree and saw the toy. She asked her mom to buy it to help. She put her arm back in the water and put the pan inside. She smiled and hugged her mum. She was very happy when he had done a special adventure. The next day, the girl asked her mum if she could go. She was so excited that she started to draw the ingredients with water. She ran around her and saw a man sitting on a bench - he was scared. She asked her mommy if she could try it. She took

**topk_10, seed 2** (150 tokens, stop: max_len)

> She asked her mommy if she could play with it. The next day, she went to the store and found lots of interesting things. She found a pretty yellow flower that she wanted to play with her. Lily felt very sad. She asked her mom if she could have a picture of her own toy. She thought it was pretty and said, "mommy, can we play with this, lily?" she asked. Her mom gave her a big, red ball. Lily was so relieved and she started to cry. She said, "you have to go on an adventure." she went inside and started to eat. She was so scared that the little boy was so happy to have helped the cat and his family. "Thank you, timmy

**topk_10, seed 3** (128 tokens, stop: eos)

> She was walking up. She started to cry. The bird was scared and she wanted to take a break. She asked her mommy, "how does I see it?" her mom asked, "can you teach me to be careful and have enough money?" her mommy smiled and said, "I know we love, but be careful, too." lily felt bad and said, "I'm glad you like her friends, so you can have it back." lily and her mom played on the swings and went to the kitchen. They saw many other dogs and the flowers. Lily was happy to have some cookies and milk.

**topk_10, seed 4** (150 tokens, stop: max_len)

> She wanted to make new friends, so she asked the other kids. "Let's go to the park. Can we go in the mailbox?" lily said. Mom said, "yes, mom. Can you help me clean my house?" mommy said, "yes, mommy, you are such a great job!" so, they went to play in the park together, but it was too hard to eat her food. So, the two friends went to the store and started running towards the slide. The water was big and cold. But the little boy was too scared to go outside. He saw an enormous rock and he started to play. He started to cry, so he decided to get a big bite of him. Timmy was

**topk_40, seed 0** (150 tokens, stop: max_len)

> She hugged her and said, "oh no, max! Can I go to the toilet?" lily asked. She pointed in a big mirror. She saw a big dog flying by him. The cat was scared and was sad. After a few seconds, the bird started to feel scared. The little girl was very sad and sad. Then, an old lady came outside to get her passport. Her mom told her that it was going to help someone else. "Can we go to a party in my backyard?" her mommy said, "no if we can play with your friends again." the man was happy and thanked lily and hugged her. She said she'd take care of the picture. She went to his garden and hugged her

**topk_40, seed 1** (50 tokens, stop: eos)

> She looked at the calendar and asked her what happened. She told all her about the world but then she stopped working. And she had no more fun. The little girl was so proud of herself - she couldn't wait to play with her friends.

**topk_40, seed 2** (150 tokens, stop: max_len)

> She asked her mommy if she could know her tooth and said, "don't worry, I'll help you fix the fridge." amy nodded and followed them to the garden. Suddenly, daisy had caught a big bag of cheese. Lily asked if she wanted to play with her. But her mom said it was going to clean a box because she was sad. She ran to the garden she saw the big tree in her garden. It was big, blue, blue dress and many colors. It was so beautiful! Molly said, "let's put the flower back on the couch." the little girl's mommy explained that they were wrong, but her dad said they needed to have an idea, so lucy went back to the store and saw

**topk_40, seed 3** (140 tokens, stop: eos)

> She was walking up. She started to slip. The sun was hot and they both had to stay afloat. But when jane woke up, when she looked up, a girl came to her room and saw her mom walking. She was upset and didn't know what to do. She knew she had to play with her doll. They started to fight and make a mess on the wall. The first little girl was sad because she didn't know what to do. She had a problem and didn't want to play at it. She tried to get the pot away, and it looked like lily's car. From then on, she knew that everyone was very careful and that was a good thing.

**topk_40, seed 4** (150 tokens, stop: max_len)

> She wanted to pick some candy, so she asked the other kids her friends. She went to the park with her mom and dad and said, "mommy, what are you doing?" she asked. "It looks time," replied lily. "We have to pay inside." lily was sad because she was excited to try it. Lucy's friends had to wear their food and started to cry. Lily tried to grab lily, but it was too late to go on. She couldn't believe it. She reached for her but to make her room feel better. She started picking up the pieces and fell down to find something new. Finally, the old lady saw a little mouse and said, "hi, I am a baby dog.

**topp_0.9, seed 0** (142 tokens, stop: eos)

> She hugged her and said, "oh no, max! Can I go to the toilet?" lily asked. She pointed in a big mirror. She heard a loud sound. It was a loud noise and blew out of the hole. It was old and lush. The fence made lily feel sad. She held it and lily's mouth tickled the nose. The little girl ran after her and she skipped to the playground. It was white, but the little girl couldn't pick out the fire. Just then, her mom saw the tear and thought she was feeling so big. She got to enjoy the sack and put it on her back. Amy was so happy to make a new friend with her family.

**topp_0.9, seed 1** (57 tokens, stop: eos)

> She looked at the calendar and asked her what happened. She told her to be careful and but the key was okay. And she had completed the unique party to play with the toy. After the doctor was gone, she said goodbye and wiped the movie and said goodbye to her mom.

**topp_0.9, seed 2** (125 tokens, stop: eos)

> She asked her mommy if she could know her paper and said, "mommy, can I give this pan?" she asked. Mama went to the kitchen. She hugged her mom and said, "oh, you need to talk to my old doctor." the brave girl walked back home and hugged her grandma tightly. She learned a valuable lesson that day, even if it's okay, she should do very nice and share. She made sure to always listen to her mom and read a new adventure and every time she did the exercises. From that day on, lily always wore sure to overcome things from that's vacation.

**topp_0.9, seed 3** (150 tokens, stop: max_len)

> She was walking up. She started to slip. The sun was hot and they both had to stay afloat. But when jane woke up, the boy didn't find a rock. It was very fast and just couldn't find his hurt one. He asked his dad, "do not know how to use your red shoes, it's too high for my project, I can't hear him." jill tried to help her, but her mom said it was okay. Lily was sad because she didn't want to play with them anymore. So, they did not permit them to go to the airport, so they ignored the ice cream cone. As they played, jane's friend called her mummy. They looked around and saw a little boy. "

**topp_0.9, seed 4** (51 tokens, stop: eos)

> She wanted to succeed. She asked the doctor why the other spell was deaf. She thought it was probably fun and it started to rain. Lily felt bad and went back to her mom. She followed her mom to grandma and gave her a big hug.

**topk_40_rep1.2, seed 0** (25 tokens, stop: eos)

> She hugged her and said "thank you okay. I didn't want to share with others, but you should be polite!

**topk_40_rep1.2, seed 1** (60 tokens, stop: eos)

> She looked at herself for telling her to be careful. But he had no choice about the toy car. Timmy ran back home and said she was okay because the doctor refused for him. After that his mom explained she would help him find it again tomorrow and timmy didn't let anyone fix his own.

**topk_40_rep1.2, seed 2** (60 tokens, stop: eos)

> She asked her mommy if he was able to make a new sandwich for tim on it. After dinner while they were walking up, timmy went home and saw them so much that his mom told him he wanted to share and find something. They played hockey all day, and he couldn't wait attention!

**topk_40_rep1.2, seed 3** (60 tokens, stop: eos)

> She was walking up when it started to slip. The sun shone down at max's web. "I know this is now!" sam said. He opened it a rock and fell into it. Suddenly, an angel appeared too far and made lots of fun for his friends in their backyard together.

**topk_40_rep1.2, seed 4** (128 tokens, stop: eos)

> She wanted to pick some candy canes and put it on top of her mouth. She went closer to herself when it was a perfect snack! When they reached the bottom, the little girl found its best toy in it with both hands, until she was still smiling about all. Jane smiled as he walked away around the park without dropping the rock. Lucy's friends had to be careful and listen to their mommy who would talk for another party, but it was too late to go home. She couldn't believe that her mom said no before it to make her feel better. Everyone loved going inside in circles and learning amazing things to find things.

### LSTM

**greedy, seed 0** (118 tokens, stop: eos)

> She asked her mom if she could go to the park. Her mom said yes and they went to the park. When they arrived, they saw a big, scary dog. The dog was very friendly and wanted to play with it. The dog was scared and ran away. The dog was scared and ran away. The dog was sad and scared. The dog was sad and scared. The dog was sad and scared. The dog was sad and angry. He wanted to play with the dog. The dog was scared and ran away. The dog was sad. He had a bad ending.

**greedy_rep1.2, seed 0** (103 tokens, stop: eos)

> She asked her mom if they could go on a trip. Her mommy said yes and they went outside. As they walked, they saw a big tree with lots of leaves. It was so pretty! But then, something strange happened. The rain started to rain. The wind blew and the sun began to move. The sky was dark and the water was gone. The little girl was scared. She ran away from the park. She felt sad and worried. She wished she had been able to help her mom.

**temp_0.5, seed 0** (129 tokens, stop: eos)

> She asked her mom if she could go to the park. Her mom said yes, but they still had to be careful. They went to the park and saw a big dog. The puppy was very friendly and he wanted to take the ball. He said, "mommy, can I go home?" her mom said, "sure, but you have to be careful with your toys." the boy smiled and thanked her. He said, "yes, please. I will help you." the little girl was very happy. She went back to the park and played with the toy. She was so excited to have a new friend.

**temp_0.5, seed 1** (150 tokens, stop: max_len)

> She wanted to make a house for her family. She saw a big, scary dog. The dog was barking and scared. The dog did not want to be scared. The dog ran away and he was sad. The dog was very sad. He wanted to play with the dog. He ran away with his dog. The dog was not happy. The dog's dog was very sad. He had a big smile on his face. He didn't like the dog. He was alone with his dog. He wanted to play with the dog and the dog. He cried. The dog barked and wagged his tail. It made a loud noise. The dog jumped into the hole. He ran away. He saw the dog and the cat. He was

**temp_0.5, seed 2** (111 tokens, stop: eos)

> She asked her mommy if she could play with it. The puppy said yes, and he went to the zoo. As he walked, he found a big, round boat. It was so big and shiny. He wanted to catch it and see what it was. He grabbed a stick and said, "look, mommy! I'm here to go here!" the boy smiled and said, "ok, but be careful." the two of them became friends and they played together until the sun went down. They were happy and proud of them.

**temp_0.5, seed 3** (79 tokens, stop: eos)

> She wanted to know what it was. So she went to the park and saw a big, bright, scary animal. The dog was scared and scared. The man ran to the man and told him that he should not take it home. The dog was very sad, and he was so happy. He thanked the farmer and went on a walk. He was happy to have a new friend.

**temp_0.5, seed 4** (150 tokens, stop: max_len)

> She wanted to make a shiny cake with her mom. She thought her mom would be a good job. When they got to the park, lily saw a big tree. She wanted to climb it, but she couldn't. She asked her mom, "can I help you?" her mom smiled and said, "yes, let's go." they went to the park and saw a big, scary boat. It was very big and had a big splash. The girl said, "look, mommy! I have a big bag to make you feel better!" she put the bottle in the water and started to get wet. Suddenly, she heard a loud noise. It was a big, scary dog. The dog was barking around the

**temp_0.8, seed 0** (72 tokens, stop: eos)

> She asked her mom if they could go to the beach for a while. Then, her mom gave her a big hug. It was a very interesting machine! They were so happy that they put the flag on the wide plane. When the bus arrived, they were so happy! From then on, they learned to be careful and not be lazy or mean.

**temp_0.8, seed 1** (113 tokens, stop: eos)

> She bent down to see what it was. She grabbed some energy all of her scarf and tiptoed to the door. She grabbed some bread and went to the bathroom. She looked around and saw a fairy. The puppy was smiling and wanted to get the puppy back. But then, it started to rain. The little girl cried. She ran running and said, "mommy, I'm sorry. I just wanted to know what we do." her mom said, "don't worry, it's my dad. He just wanted to make a beautiful day."

**temp_0.8, seed 2** (150 tokens, stop: max_len)

> She asked her mommy if she could know what it was. Her dad smiled and said, "this looks like a good job." he nodded and followed them to the front. Suddenly, the water started to rain and the sky was poor. It landed on the floor and started to burn. The people in the park were happy and said, "here, let's play with them, but we can't get it." so the two block started to walking towards the lock. Suddenly, they saw a little girl with a big smile on her face. "Who's the apple?" the little girl asked. "You should be patient, but you don't want to belong here. I'm glad you could come back soon." lily

**temp_0.8, seed 3** (150 tokens, stop: max_len)

> She wanted to know what it was. So she went to the park and picked it up. She tried to play more, but it was too heavy for her. She put her hand on the ground and just walked away. She was delighted and excited. She was able to do that first she wanted to play with her friends. On the way, she had a dream that was just a stranger. She tried to take her board and get up. But it seemed to be friendly and she didn't want to leave. She thought for a moment for the girl's help and sorry to her. Finally, the tired lady called her, "what can I do to do that?" the lady smiled and said, "sure!" the girl followed

**temp_0.8, seed 4** (79 tokens, stop: eos)

> She wanted to succeed. She asked the little girl about the spell. Her mom said yes and had a great time. She was so excited when they finally found it. The little girl was so happy. She showed her friends that her grandma was very old and thoughtful. She was excited to see her mom even more. She put hands and ice cream, and it was the best person ever.

**temp_1.0, seed 0** (150 tokens, stop: max_len)

> She lay down and started walking in the water. As she was scattering along, she saw a small boy with a shiny bow in his hand. She was so excited, but he stepped very tall. He couldn't believe he ran away! But when the little girl opened the fence, she saw that the other warning was and stopped so much that the mean man told the present to get her scarves. They both got angry and threw the white arm on the ground. "Hey that was fun!" she said. The brown man looked at her. She stopped crying and asked him how late it was. The man was happy and said, "I don't want to leave in it!" the little girl was disappointed, but she knew the jewelry

**temp_1.0, seed 1** (119 tokens, stop: eos)

> She bent down to see what it was. But then she stopped all all about about the window. She stopped clapping and smiled. She did not want to be worried. The next morning, dad noticed that the grass were appear on the floor. He was allowed to be safe, but he knew he had found his angry news. He put the snowball down in his pocket and smiled. His mom gave him a treat with her pile of lemons from the box. Then it sailed through the sky, with a lot of love. After that, he presented the pill for a journey. The end.

**temp_1.0, seed 2** (150 tokens, stop: max_len)

> She asked her mommy if she could know what it was. Her dad smiled and said he could use something else. As he got there, he noticed some scissors and put on his best coat to stay. He slowly walked over to the poor old man, feeling the brave soldier who died. The store said goodbye, going to the house and then started to cry. Suddenly, a familiar, smelly juice blew out. It was a bad little girl, she was walking towards the man. She smiled and wiped her arm tight with water. It was startled and started to cry. Mommy said, "I don't have my thank you every day." the little dad smiled and said "well. I'm glad you could come back soon. She will

**temp_1.0, seed 3** (150 tokens, stop: max_len)

> She wanted to know what it had. So she guessed her parents who wanted to build the top. She pulled up a cloth together and began to drift them. It made her favorite face very high and smooth just like the naughty animals. She asked about how fast she found and decided to walk down the street. Then, they heard on a puppy with a funny rabbit. He couldn't believe that he had disappeared. He pressed it and saw a group of neighbors playing with people. She was wearing a number of garden at the park. He was so happy to see the sun run off to go away, so he decided to turn off again. He was sure to see that it called the bank. So, the pig had to be careful. He

**temp_1.0, seed 4** (97 tokens, stop: eos)

> She wanted to succeed. Her mom and dad looked about the dishwasher. They looked at the wonderful staff. They wanted it a rug and then it smelled sweet. After the parade, it was time for dinner. It was time to go home. The old lady said goodbye. Inside, she found a thick hedge. She was so happy and excited that she used it to write for food and all around. Everyone on the stage was very happy. However they were safe in the sky.

**temp_1.2, seed 0** (143 tokens, stop: eos)

> She lay down and started walking in the middle between her hand. However one answered, her favorite's room was no longer dirty and croaked. Sadie then became a pinch knowing it was time to go inside. She slowly went out and turned over. She found a lush animal safety! She ran to her mother in warning. And the ball washed her daughter. Daddy told the present to end her scarves at her town before eating her cones. From that day onwards, the old bear sang time when a few days he spent her way forever. The boy sang up sometimes its soaring, keeping off and wore some honey. Before she was out of breath, amy remembered the rose with her new sack and it made her happy.

**temp_1.2, seed 1** (122 tokens, stop: eos)

> She bent down to see what it belonged. She grabbed some energy all all around outside and tiptoed inside. But then she dropped her diary and went back to the library. The classroom smelled bad and so there couldn't keep appear on its truck. The cabin sank at her and she thought it was disgusting. She started so soft that she noticed that the lamb had become orange and noisy! The little girl stayed with the broken white flowers and the animals were both by her fake head that it got gone. Lily and she clapped and laughed. The girl happily opened the cabinet and searched for the peace memories, again.

**temp_1.2, seed 2** (129 tokens, stop: eos)

> She asked her mommy if she could know what it meant. At her mommy stood and looked in anticipation. When they walked up, mama went home and saw them pennies. Questions for her that at her side, she was so excited. Poor albert introduced a feeling of the stitch who smelled mel and seemed smarter in his wife reappear. But when he started to cry, the boy gave them, she felt even beat there. Her mom started working up block, but walking above the lock. She used it to laugh, and mysterious dreams of happiness singing them. Soon, the first cheese were out breathing, after lila's foot thank everyone every day.

**temp_1.2, seed 3** (150 tokens, stop: max_len)

> She wanted to know what it is. So she guessed her parents who wanted to build back. "I know this whole would dream," when the little girl got a rock. It looked super a lawyer just like the naughty puppy. She asked about how fast she found and did not know how boat it was. Then, it on a puppy with another shoulders, worse, and that it made a little feel a messy man forever he couldn't. Daddy was excited and started eating and head into a playground of garden at catch them. He was so happy to see the sun run off to go there, so tired then he said, "hi bye! Can you help me improve called the bank?" her wife smiled and said, "this is

**temp_1.2, seed 4** (150 tokens, stop: max_len)

> She wanted to succeed. Her mom and dad looked about the spell. They looked up and saw an old lady. It a rug and thought it would happen. After the parade there was different, the 3 year old child explained that "useful I was hidden to flowers.. Inside are scary, cold bellies". "He wanted to find something that". The mommy and dad looked at all around. Who cracked there, she recognized that the hands became weird. "Look, dad!" the man smiled excitedly. "Freeze yet everyone to wash slowly!" the bully loved bowing sadly in the wild line but he said, "don't forget you can do the sweetest boat!" go to the mug and woke by mrs arriving - popping into

**topk_10, seed 0** (51 tokens, stop: eos)

> She asked her mom if they could go to the beach for a while. Her mom replied, "yes, but be gentle and be careful. It can be fun, but if you don't have some ice cream and it will be very good."

**topk_10, seed 1** (143 tokens, stop: eos)

> She wanted to make sure it was a special place. She was so excited to have the best time. But then she saw something very strange. It was the wind! The kids looked everywhere and saw the sun. It was an old man who was carrying his hat away. He was amazed and asked his mom if he could get to the man. The boy said yes and they both walked to the park with the old man. He said goodbye to the man and they walked through the park, holding hands and jumping. After the day, the man waved goodbye and went back to the beach. He was happy and proud about how he had a great time. He was happy he had helped the old man again.

**topk_10, seed 2** (129 tokens, stop: eos)

> She asked her mommy if she could play with it and play with her. She said she could use the scissors to keep it safe. She told her it was a toy that it could be so much fun. The girl was sad because she couldn't do it, but she knew she was going to help the people who was trying. The old boy was sad and said, "I want to play with my ball!" the boy was so excited! He grabbed the ball and took a bite. It was the best thing ever! It was so cool and he thanked the little boy. He waved goodbye and played with his toys every day.

**topk_10, seed 3** (150 tokens, stop: max_len)

> She wanted to know what it had. So she went to the park and looked at the flowers. She noticed a bright rainbow in the sky when she looked up. She saw a man who was a boy. He said to him: "hi! What are you doing?" "yes, we can play together," said the man. They were having a great time. When they arrived at the old man's man, he saw a man who was very excited. He was wearing a special uniform and said, "this is an old man. He said, and it's just a toy," he said. The boy was happy he was smiling and wanted her to have a picnic. So, the little boy went to the store.

**topk_10, seed 4** (150 tokens, stop: max_len)

> She wanted to make a new surprise and put them in her pocket. Suddenly, she saw a big, scary cat. A kind dog came and said, "hey, I am a dog!" he said, "hi, my name is the dog!" the girl thought for a moment and said "I want to see the dog." "you are my hero!" he said. He barked at the man and he gave the cat a big hug. The dog said, "thank you, lily. You are very brave to meet you." the dog barked and ran away with a big dog. The dog had long hair and curly fur and a long tail. Lily and the dog were happy. They ran around the dog and

**topk_40, seed 0** (150 tokens, stop: max_len)

> She asked her mom if they could stay in her room for a while. Then, her mom took her to a big city near a big tree. The wind made a loud noise and it seemed very cold outside. Lily was sad because she had seen the little bird in the park. She wanted her mother in the garden and asked out what was wrong. Daddy told the mommy what it was and the woman told them to be careful with the toys. The little girl nodded her head, and finally walked out of the park and saw the clouds shining. She stopped feeling so relaxed and ran away. But when the bird was getting out of its yard, it stopped and saw her mom struggling to visit her. She was wearing a small towel and the little

**topk_40, seed 1** (80 tokens, stop: eos)

> She wanted to put some jam in the water. She saw a girl and asked about the dog in her bag. She smiled and said she was okay. The little girl wanted to help her dad so she ran by the tree and said yes. The lady said goodbye, and she gave them a kiss. The little girl took this to school. Then, they sat down and enjoyed her tasty snacks.

**topk_40, seed 2** (107 tokens, stop: eos)

> She asked her mommy if she could ride her cart and said, "yes, mommy. I'll help you find something." mama went to the kitchen and sat on the seat. She grabbed her plate and started to put them in the sink. She was so excited to be the most beautiful things. She hugged it and danced. When she started to get back, she gave them some cocoa juice. She was sure to be friends with her best, but she was always able to try new things and make the most beautiful shapes.

**topk_40, seed 3** (150 tokens, stop: max_len)

> She wanted to know what it had. So she went to check the book in the garage. She tried to reach it, but it was too heavy. She got a rock and quickly ran to the living room. The machine turned on and the girl started to cry. She did not know what to do. Then, a girl on a noise with a loud noise. The girl was scared that the little girl was sad. Luckily, the man got scared. The monster had a problem and the doctor couldn't play at it. He was so angry they did it. He knew he should help him, so he gave the dog some water to use his tail to make her feel better of better. The little boy was scared and ran away. But

**topk_40, seed 4** (140 tokens, stop: eos)

> She wanted to pick some water, so she looked around and saw a big, round tree. The butterfly was filled with a white blue dress and a sweet blue coat. The little girl was so happy. She ran and ran and ran until she was still laughing. Suddenly, a gust of wind blew and around the park. It moved around and down, and it seemed gone for her. It was stuck with many people for the whole, black blue ball. She was happy, and she couldn't believe her eyes. She ran out with her mommy, and they hugged each other tightly. In the end, the man said goodbye and smiled. He was happy that he could have fun with it.

**topp_0.9, seed 0** (150 tokens, stop: max_len)

> She asked her mom if they could stay in her room for a while. Then, her mom took her to a big city. She was very enthusiastic to tell her mom, so they gave her a big hug. Lily was excited to see what she had and loved to walk. She ran to her mother's house, and asked for a few minutes. Her mom said yes and she showed her the pictures. The teacher went to the bathroom, and bought the olives. She said, "welcome, mommy!" her mom smiled and said, "yay!" the big building got mad and said, "don't worry, sara. It's a really messy pair. It's too big for you." after they finished, they hugged back

**topp_0.9, seed 1** (135 tokens, stop: eos)

> She wanted to put some gems in the water. She saw a fisherman and threw them to the puppy's hand. The dog ran towards the rescue and tried to get away the fish. Suddenly, he heard a loud bark. The boy's parents heard him and came to see what was happening. They saw the puppy so much that he had seen them. They wondered if he lost the dog. The man put the broken white pile of some from the fire and then it sailed away. The animals were so relieved that he gave the dog the frog some corn. They thanked the wise man for being safe and happy. The boy took the branch from the man and said goodbye.

**topp_0.9, seed 2** (150 tokens, stop: max_len)

> She asked her mommy if she could know what it was. Her dad smiled and said he could use something else. As he got there, he noticed some scissors and put on his best coat. He asked him, "what do you do?" a little boy said, "I'm going to replace it, but it's a surprise." she took a deep breath and said, "yes, I can take it." but soon, the doorbell stayed up and the little girl smiled. She asked, "don't be good at them. You did it for." the child smiled and said, "thank you, farmer. You are very clever." the man smiled. He said, "yes, you can have it,

**topp_0.9, seed 3** (109 tokens, stop: eos)

> She wanted to know what it had. So she went to check the book in the garage. She tried to play more more. When she got there, she got a bigger drops. She reached a trap and was so excited. She quickly jumped back into the bucket, and smiled as she reached the top of her arms. Then she saw a big rock in the garden. It was a beautiful treasure and a silver view. It was so pretty that it was beautiful. The girl and her mom played on the garden and had lots of fun.

**topp_0.9, seed 4** (150 tokens, stop: max_len)

> She wanted to succeed. Her mom and dad looked at her each castle and thought that it was cool. They decided to go out and play. They walked around the lake until there was a picnic filled with light. They both had a lot of fun at the park. In the park, the cold rang mentioned to repeat for kids. It seemed so cool. It thought it was a moment. It liked to cry and throw away. The mommy was surprised. She said, "dad, I wish we were not our best." everyone's mom said, "we're feeling scared. I'm sorry I can't play." the little boy was angry and started to cry. Lily and her mom ran away from the tree and saw that the

**topk_40_rep1.2, seed 0** (77 tokens, stop: eos)

> She asked her mom if they could stay in her room for a while. Then, her mommy gave her a stamp and a new blanket. Molly was very excited to have it back with big smiles. She couldn't wait to take the medicine home when she went for an elevator! From that day on, she was extra careful and never forgot everything she had seen with the mirror before.

**topk_40_rep1.2, seed 1** (103 tokens, stop: eos)

> She wanted to put some jam in her hands so she started walking. She grabbed a blanket but then she stopped moving. "What's wrong?" asked the little girl for a while. "I don't know what do we look here?" "we can't let them fix it," said anna. So they sat around the park and had so much fun together. After the bus was done with the ice white balloon tried again and continued playing by the rain made that it disappeared into her warm air.

**topk_40_rep1.2, seed 2** (150 tokens, stop: max_len)

> She asked her mommy if he could ride her cart with him, but it was just hers. The little girl nodded as mommy watched her go and soon it was a big surprise for her. At the bottom of the house, there was a little puppy that was a large cat who liked to use things. The boy was so happy. He jumped back and ran back to tom's toy, holding his bag very much. When they got home, lily said "let me see what I will have!" her mom said with a gentle face from them. The lady grabbed the ice apple out on the stove and took it home. They all started playing the little bear while they went past their own things, and in a huge house, he was so

**topk_40_rep1.2, seed 3** (131 tokens, stop: eos)

> She wanted to know what it was. So she went back home, excited that all the animals were different more things. Then the little girl asked her mommy if it would come true. Her dad told them her mom said that they needed to stay close when they worked. And she smiled at mommy, so he made sure to be dependable too. At first, when she got out of her house, she saw a group of old animals playing with toys. It seemed like someone came and took turns to sing something special at night, but her parents gave they to put up and run off to go there. Soon, lily's dream would be happy again!

**topk_40_rep1.2, seed 4** (144 tokens, stop: eos)

> She wanted to pick some water from the garden and put them in her mouth. She found out on herself's shirt and started looking at it when they saw a big lake. There was different trees that had fallen down with lots of grass until there was a new place. It was very loud and cold. "What's wrong?" asked mummy. "You had to be careful," said mommy. "Don't worry, lily, you have to find something to go home. How about your boat will give our puppy to the store to make sure I think we're too scared!" he looked under the tree to find some new animals and rocks. Then the bear ran away. It was a good adventure.

## P3_unexpected_ending (an unexpected ending)

**Opening (human-written):** Max worked all day to build the biggest sand castle on the beach. He was very proud of it, but when he came back the next morning,

Prompt words outside the RNN/LSTM vocabulary (seen as `<unk>`): none

### Vanilla RNN

**greedy, seed 0** (61 tokens, stop: eos)

> He saw a big, scary dog. The cat was very sad and wanted to help. The bird flew away and the bird flew away. The bird was so happy and thanked the man for helping him. The little boy was so happy and thanked the man. He was happy to have a new friend.

**greedy_rep1.2, seed 0** (97 tokens, stop: eos)

> Timmy's mom told him that they were going to visit his friend and asked if he could go outside. So, tim went to the park with his mommy. He saw a big tree in the sky. He wanted to play with it, but he couldn't find it anywhere. Suddenly, he heard a loud noise. He looked around and saw a little girl named lily. She had an idea. She said, "I'm sorry, sweetie. You are my best friend!"

**temp_0.5, seed 0** (100 tokens, stop: eos)

> He saw a big, scary monster. The cat was very hungry and wanted to help the bird's name. The bird was scared and tried to catch the rock. The dog was very happy. He wanted to help his mommy. The old man smiled and said, "let's go to the park." they went to the store and bought the food. The little boy was so excited and he started to climb the top. He was so happy that he could help the bird. The end.

**temp_0.5, seed 1** (150 tokens, stop: max_len)

> He saw a big, scary dog. The mouse was very happy. He wanted to explore the world. But he did not know what to do. He looked around and saw a big tree with his friends. He wanted to play with it, but he didn't know how to fix it. Timmy didn't want to share his ball, but he had no friends. He decided to give the ball to his friend, so he asked his dad if he could go outside. He asked his mom, "what's that?" the boy said, "I'm sorry, timmy. I won't do it again." the boy was so happy to have a new friend. He thanked the old man and went home with a big smile on his

**temp_0.5, seed 2** (101 tokens, stop: eos)

> He saw a big, red ball. The cat was scared, but he knew he had to be careful when his friend was gone. He told him that he should not be patient and not to be sad. He said, "you should be careful, but I'm glad you are brave and smart." the little boy was so happy to have helped his mom. He gave them a big hug and said, "thank you, little girl," said lily. "Thank you, mittens!"

**temp_0.5, seed 3** (136 tokens, stop: eos)

> He saw a big, scary cat. He was so excited! He wanted to get closer. "I'm gonna know what you can do!" the rabbit was excited to help. He reached the top and saw a big tree. He asked his mom if they could have some of him. So, he decided to try it on his own. He tried to jump on the wall, but he couldn't find it. Luckily, he saw a big, beautiful object. It was a big, red ball. He picked it up and showed it to his mom. He was so happy and excited to have a new friend. He was happy to have found the perfect spot!

**temp_0.5, seed 4** (49 tokens, stop: eos)

> He saw a big, shiny cat. He looked around and saw a big, round tree. The bird was curious and started to move. The man was very happy and thanked the man. He was so happy to have saved his new friend.

**temp_0.8, seed 0** (150 tokens, stop: max_len)

> He saw a bird. His mommy told him that it didn't matter what to do. He started to panic and had a new picture of his friends. He wanted to try it, but his mommy told him not to worry. He regretted not using his envelope and told him that he should be careful for him to be and share. He then ate an old flashlight in the tub and tried to take it home. But when he got to take a closer, the old man said, "I will help you find the way forever." tim was so excited! He hugged the bear and showed him how to fly away. The little girl was so happy to meet her new friend. From then on, she would wake up and make others all about

**temp_0.8, seed 1** (54 tokens, stop: eos)

> The bear realized that the lion was fixed. He realised that he had to obey a bad job. He was glad he could talk to the bird and be the best of friends. Timmy and dad spent the food of the tree together and they all lived happily ever after.

**temp_0.8, seed 2** (150 tokens, stop: max_len)

> He saw a big surprise. He jumped and he added some cream in the water. He used the tools to make a happy song. He loved to show them how to make it best. At the end of the day, timmy's poor old man was feeling proud of him for being brave and smart. He hugged him and said, "thank you, timmy! You should be very careful with his new toy. It was my favorite toy! I think you'll smile soon!" she smiled and waved back. When she got home, she told her mom would be polite. She said, "don't worry, thank you. I'm going to spread dad to make a mess." the old lady smiled and said "thank you, lily

**temp_0.8, seed 3** (150 tokens, stop: max_len)

> He saw a big, scary cat. He liked the ball and watched it fly all day. When he arrived, he saw the little boy when he saw the man a toy. It was a sunny day at the bottom. They went to the store and bought some food and decided to walk down the street. John was scared, but he knew that he had a plan for his friend. Timmy decided to try a carton of the drawings so he could have it back. Billy was happy to hear the number of the dog's toy for her. So they went to the store to buy some candy. They put some cream in the cup and sat down from the bookcase. The little boy was very excited to play in the garden and play with the toy

**temp_0.8, seed 4** (36 tokens, stop: eos)

> She saw something shiny. It was a big, red ball. Her mommy came over and saw the mess. Lily was a bit scared again and they all lived happily ever after.

**temp_1.0, seed 0** (145 tokens, stop: eos)

> Timmy's mommy said yes. Timmy realized that he needed for something to make his paw feel better. Timmy knew no one was new enough, but he was too young to try. He gave him a big hug to wide, and the microphone was fierce. The bird gave the little penguin bob to the mother's warning. And lily learned how to you be a special gift instead of it. From that day on, lily went to bed with her new friend. The old lady said, "would you like to stay around and play with me?" she nodded eagerly and gently felt better. She wiped the sack and put it on her back. Amy was really happy with her new sack and couldn't wait to play outside.

**temp_1.0, seed 1** (147 tokens, stop: eos)

> The bear realized that the lion had grown. He realised that he had to obey a bad but then he stopped working. And his mom did not listen to the man. The mean timmy saw the doctor. He said, "don't worry, he takes out my vase to protect his dog and timmy." his mommy helped him to not care and said "can I tell you how to clean the spaghetti with the red pencil?" the old man replied, "yes, that is so cool." and she was so happy. She liked her new pill for a journey. She created so much fun and laughing with her new blocks. From that day on, lily liked to play in the beach, happy with her stuffed jewelry.

**temp_1.0, seed 2** (150 tokens, stop: max_len)

> Jimmy saw a big surprise. He jumped and he added some cream in the water. He used the pan to make a happy song. He loved to keep pretending to honk questions for something else to stay. One day, timmy's mom asked him if he wanted to play with her eraser. Mittens was sad because she was worried. But then, mittens heard an enormous voice. She stopped, she saw the mitten. It was a tiny cat and a necklace. Lily saw a pair of a pony, and asked, "what is it doing? Remember" lizard asked. She looked up and saw strange things. She looked everywhere and couldn't figure it anywhere. Dad said, "I have an idea, you don't want to taste in her bed

**temp_1.0, seed 3** (150 tokens, stop: max_len)

> His mum started to play with in. So the timmy sat down to collect max's back. "I know this, timmy!" sam said. "Now it is bigger than it!" the two friends were so excited. The sun taught their happiness and they continued and decided to walk down the path. John was scared, but he trusted his friend. He kept on his board and ran away. Tommy was sad because luckily he had done something wrong. The monster had a problem and the leaves couldn't say hello. So he tried to grab the cushion away, and it looked like a fire, so he decided to pick it up. He was very careful and let was called the bank. So, the little teacher hopped over to the backyard

**temp_1.0, seed 4** (36 tokens, stop: eos)

> She saw something mysterious. It was a plastic berry about the sky. It looked like a wonderful cave. It made her feel happy and pretty. They all lived happily ever after.

**temp_1.2, seed 0** (150 tokens, stop: max_len)

> Timmy lay down from the beehive and saw a crocodile. He decided to take a nap on the grass. But no one came out of the mirror. As he sat, bobo fell asleep. Everything could reach again. Wide missed the ball after a few seconds and johny off safety! From bob was on, max held his red sweater out, then reads an old package. Johnny pose it so scarves at their town before eating eating pond off from take a tail. The old ladder sang out was a lot of movements and talking and interesting apples. He sang up and its family hugged him off. Dotty was upset again before taking his pan with his friends. Acorns woke up with her small sack and licks the boat tightly. After they finished, she hugged back

**temp_1.2, seed 1** (141 tokens, stop: eos)

> Bobby bent out to see what it belonged. He grabbed some energy all feet at the top but then he stopped clapping. And his family did not listen to the man. The mean timmy tried to stay there and tried to appear on the truck he could find out at it. Katie thought it sounded cool. His owner so soft. He put the snowball down - it mixed and tissues there began to be friendly with the red white flowers. The animals were so happy that each other was so happy, proud of them. He gave jack a juice and some medicine. They went back to the sandcastle together, reading and laughing. Sam lifted up branch from a long time, savoring for his thick adventure without days.

**temp_1.2, seed 2** (64 tokens, stop: eos)

> Jimmy saw a dog. He was excited and he added some cream in the water. He used the pan to his mouth and cut drops a flag from it. Tim hugged tim for best that to stay at him and they all had shared of fun in a hut. The room was always bouncy and cute. The end.

**temp_1.2, seed 3** (64 tokens, stop: eos)

> His mum started planting her best in. So she guessed her flute tightly and they both tore on the compass pie. Though never the nightmare, when they remain now, lily's favorite truck washed off the stove and was so happy. The sun taught janey how many seeds, and did not know how boat it was clear.

**temp_1.2, seed 4** (114 tokens, stop: eos)

> She saw something mysterious. It was a plastic berry about outside his castle. Alice was happy to see herself. Amy was a bit curious from the man. She pointed the orange that shrimp was safe. Even though it was time to return, she was still free about the storm inside. She ran up to dotty and asked her mom hands it to unlock, but it thought it was too pretty. Lily liked to cry and feelings. Lily's mommy rolled into her bedroom and had crying. She couldn't believe that her mom convinced freeze yet with to wash her room rolling.

**topk_10, seed 0** (150 tokens, stop: max_len)

> Timmy's mommy said yes. Timmy told her mom about her help and asked him, "what's wrong?" the boy asked his mom, "can I help, but please?" his mom smiled and said, "I'm glad you're my friend." the little girl was so happy to see a new friend and said, "you should be very kind and honest." lily smiled and said, "I'm glad you had a good adventure." she said, "I love you very much. I'm sure that's good. Now we can play with your friends again." the man was happy and thanked lily and hugged her. She said she would take them back soon. She said, "I'm sorry, lily

**topk_10, seed 1** (135 tokens, stop: eos)

> The bear noticed an old man. He looked up in the sky, looking at the sky. The fish was so big and strong. The lion was sad and ran away. He looked for the sky. He tried to catch the butterfly and get the ball back. But he could not get hurt. The man saw him with his ball and asked, "what's wrong?" her mom asked the man for the help. The doctor said he had to take her and his mommy. He took her back and went to the kitchen. He was so excited that she started to weep and shout. She was happy to have her own ice cream for her to keep it forever.

**topk_10, seed 2** (150 tokens, stop: max_len)

> He saw a big hill. He had a big hat and decided to eat it. He picked the button and ran to his mom. He found a big box and put on his shoes in his pocket. He wanted to find a little mouse. He tried to climb the gate, but nothing was too hard. His friend, the little boy was not sad, but he didn't understand. Timmy felt sad and angry. He said, "I'm sorry, lily. We don't know what to do. The bird will not be mad at them." timmy tried to grab the ball out, but he didn't know what to do. Then the little boy got out of the forest. He had a lot of fun. Then he remembered that

**topk_10, seed 3** (23 tokens, stop: eos)

> His mum told him a story about the world. Timmy was amazed. He had a big smile at the party.

**topk_10, seed 4** (78 tokens, stop: eos)

> She saw something shiny. It was a little puppy. The little girl asked, "why did you do it?" her mom said, "I don't need the same time. But only the truth can't do anything that you need to stay with you,". Jane smiled and said, "I love you too, lily. I'm proud of you to the store."

**topk_40, seed 0** (150 tokens, stop: max_len)

> Timmy's mommy said yes. Timmy realized that he needed for something to make his own pet. John went inside a tree! He couldn't believe it! He made more adventures and they both ran after it again. Timmy was happy when he put his car in the water and started to run away. Timmy was sad. He asked him, "you should be very naughty and don't worry, I'll help you." tim was sad, but he knew the old bear was gone. Finally, jack went outside to help his mommy. He didn't know why the big bird got mad and wanted to play with it and he started to cry. He cried and saw no one. He couldn't believe how much he had found it. The fox

**topk_40, seed 1** (150 tokens, stop: max_len)

> The bear realized that the lion had to get an old person he had to go outside and make the frog come true. The next day, timmy went to the park to play with timmy. Timmy didn't like to wear his car. They ran to the kitchen at the park, but they heard timmy's mom. He took him to school and thought to check it. Timmy was so happy. The next day, timmy accidentally started playing soccer in the forest. He was very sad. He had never found and wanted to give it right away and play too. Timmy went back to the bathroom and looked out of the lake. As he walked for a walk, he saw something special and strange. He loved to go for a ride. He decided to

**topk_40, seed 2** (58 tokens, stop: eos)

> Jimmy saw a big hill. He jumped and he heard a voice. Tim was scared. He dropped his arm and tried to save him. He felt sad. Tim got angry and decided to be sorry. He felt sad and wished. They played hockey all day, and he was happy.

**topk_40, seed 3** (34 tokens, stop: eos)

> His mum started to play with in. So the man sat down to clean in the garage. When she arrived, timmy would play with her toys and make new friends.

**topk_40, seed 4** (60 tokens, stop: eos)

> She saw something mysterious. It was a little brown cat outside his castle. She was so amazed that it was an old sight in the corner of the water. The bunny said that it was safe and special, it could lead that, until she was still to have a fun day on her house.

**topp_0.9, seed 0** (133 tokens, stop: eos)

> Timmy's mommy said yes. Timmy realized that he needed to make his own own toys on the grass. Timmy tried to bite it, but he was too busy making more noisy. Lily thought about the broken balloon. She was happy that she could help her and cleaned off the fence. She sat down and looked in the mirror and so much fun! Eventually, the little girl ran around her house and played with the music. Then, she went home and showed her mom she needed to organize a piece of paper. Her mom taught them how to behave. Max learned that it's important to ask for help the youth and share the importance of being smarter or kind.

**topp_0.9, seed 1** (80 tokens, stop: eos)

> The bear realized that the lion had grown. He realised that he had to obey a bad but then he stopped working. And his mom did not listen to the man. The mean ant saw the doctor. He said, "don't worry, he will have enough money to protect his cousins and timmy." his mommy smiled. "Maybe" and said, "yes, I can swing."

**topp_0.9, seed 2** (150 tokens, stop: max_len)

> Jimmy saw a big surprise. He jumped and he took him to a big building. He used the umbrella to make a happy song. He loved to keep them so much. When he got to the ground, he saw a shiny tree in his garden. It was green and soft. Tim said, "it's going to the house!" he brought his toy car to the mill, holding his bag - there was a weapon. It was big, blue, blue, and many colors. It was so beautiful! He said, "let's put the jam back to the mechanic." the little boy's mommy explained that he wanted to play with her dad. Tim was sad. He saw the dove in a corner. His mom was surprised

**topp_0.9, seed 3** (140 tokens, stop: eos)

> His mum started to play with her. So she went to the park and bought the pizza. She tried to play a flute together, but when she looked up, lily saw a huge little bird. Sue didn't know what to do and asked her mommy if she could have her favorite vase to say. Lily agreed to try it on her puppy and didn't know how to get it up. But then, a group of days told sarah about the pool. The daughter had a problem and a pot of soap. Lily took the train on her back and showed it to her mom. Dad was excited to have a special treat and would never lose the oasis every day before her friend called the lady.

**topp_0.9, seed 4** (150 tokens, stop: max_len)

> She saw something mysterious. It was a plastic berry on the ground. It looked like a wonderful cave. It made her feel sick and pretty. The sun was shining, and she was amazed by the ground in it. Every day, she would go to the park with her mommy. One day, lily's mommy asked her to wait until they went to play in the snow. Lily wanted to climb on a boat, but she didn't want to pick it up. Suddenly, lily's little brother she saw a photo of candy and a big rainbow. The elephant had a collar in his hand. Tim didn't want to stop playing with his friends. The chicken started to blow up and go to the reef. The mechanic was so excited that it

**topk_40_rep1.2, seed 0** (72 tokens, stop: eos)

> Timmy's mommy said yes. Lily realized that she needed for help and put her hands on the grass. Inside a tree! Ella couldn't believe it! Emma made more amazing things with big muscles. One day, lily was playing hide in the woods when they heard an elevator! From then on, lily learned to be calm and not trust anyone or break.

**topk_40_rep1.2, seed 1** (107 tokens, stop: eos)

> Timmy saw a big rock. It was soft and red! He had swum at the top but then he stopped working. "What's wrong?" tim looked around him for making some noise and his friends ran by. They were worried and didn't know anymore at first. Joe thought it sounded cool. His owner wanted no food to come with them. So he grabbed a ball and began to squeeze off with the shampoo. When he got home, he said goodbye and made that it hurt his toy car and ate his toy face.

**topk_40_rep1.2, seed 2** (28 tokens, stop: eos)

> Jimmy saw a big hill and decided to use it with him. Timmy thought it needed hard work, so they ran in his mom again.

**topk_40_rep1.2, seed 3** (32 tokens, stop: eos)

> His mum started to play with in. So she went her flute tightly and they both had fun together, making new friends around the house again when playing outside.

**topk_40_rep1.2, seed 4** (150 tokens, stop: max_len)

> She saw something mysterious. It was a little brown cat outside his window. She turned her closer on it and made it go out of sight! They started walking around the house that it found its best. Everyone cheered at each other, until they looked at the flowers. "What do you want?" "I want to see my bag!" "you are my hero!" tom says. He holds on the paper door in his bucket. Anna feels happy and sleepy. Mom hears him stop she knows who have broken. She comes to lily. She sees sara. She sees not in the kitchen. She picks up the doll with mia and licks the cookie. She tells them not to touch the book. She starts to cry if she was

### LSTM

**greedy, seed 0** (73 tokens, stop: eos)

> He saw a big, scary dog. The dog was scared and ran away. The dog was scared and ran away. The dog was scared and ran away. The dog was scared and ran away. The dog was scared and ran away. The dog was very sad and scared. He was scared and scared. He wished he had been brave and he was safe.

**greedy_rep1.2, seed 0** (150 tokens, stop: max_len)

> He saw a big tree with lots of leaves. He wanted to climb it and see what was inside. He asked his mom if she could go outside and play. Her mom said yes and they went to the park. As they walked, they found a big hill in the sky. Tim was so excited! He ran around the yard and watched the sun fly down. He laughed and clapped his hands. Suddenly, he heard a loud noise. It was a little girl. She was scared and ran away. She looked at the dog and said, "I'm sorry, mommy. I didn't know you can't get it." the man smiled and said, "don't worry, I'll help you." the boy nodded and said

**temp_0.5, seed 0** (103 tokens, stop: eos)

> He was very tired. His mom told him he needed to make sure it was safe and he could keep it safe. Bob's mom was very sad and asked him to help him. But then, he saw something strange in the grass. It was a big, scary dog! Max was scared and ran away. He knew he had to go home. He told the puppy to go back to the park and play with his friends. From that day on, the old man was always careful and never helped anyone.

**temp_0.5, seed 1** (126 tokens, stop: eos)

> He saw a big, scary dog. The dog was scared and wanted to play with the dog. He ran to the dog and said, "I'm sorry, tim!" the dog smiled and said, "I'm sorry, tim. I don't want to play with you." the dog said, "no, I'll help you." the dog was very sad. He had a big smile on his face and said, "I'm sorry, tim. I don't want to play with you." the dog and the dog ran away. They played with the dog, and they were very happy.

**temp_0.5, seed 2** (150 tokens, stop: max_len)

> He saw a big, green pebble. It was a big, shiny toy. It was a big, shiny ball in the sky. He wanted to go inside and play. He decided to be careful when he saw a big, scary animal. He tried to climb the tree but the rock was too strong. He was scared and didn't know what to do. Suddenly, he heard a loud noise. He looked around and saw a little girl. She was walking towards the man. She was scared and asked, "what is wrong?" she pointed to the man and said, "I know, I'm going to catch it!" the little girl smiled and said, "I'm glad you're safe, but you need to be careful

**temp_0.5, seed 3** (117 tokens, stop: eos)

> He saw a big, scary cat. It was a friendly cat who was walking towards the tree. He was scared, but he wanted to play with the cat. Lily's mom said, "don't worry, tim. I will help you." the little girl and her mom went to the park to play. They saw a big, white dog. The dog was barking and had a long tail. Tim wanted to help the dog, but he was scared. He ran away and walked away. The dog was sad, but he was still happy to have found the dog.

**temp_0.5, seed 4** (150 tokens, stop: max_len)

> He saw something shiny. It was a big, red ball. He wanted to play with it, but he wanted it. But his mom told him to stay close and take it home. Max was sad, but he wanted to keep the big, but he was too weak. He got frustrated and started to cry. He wanted to go to the park and play with his friends. But then, he remembered his mom's warning. He said, "I'm sorry, mom. I should have listened to your mom." his mom hugged him and said, "it's okay, tim. Let's go home and get some water." tim nodded and said, "yes, it's okay." his mom smiled and said, "

**temp_0.8, seed 0** (141 tokens, stop: eos)

> He lay down and started his adventure. When he came back, he saw a big, colorful balloon. It was shiny! Max croaked at his dad, and he jumped back. He held his hands tight and slowly went inside. When he got there, he saw that the fence was so bright and shiny in his toes and he wanted to use the treasure. He giggled and ran around the house. They found a playground that had many trees, and the sun was old. The sun was shining and it was sunny. Max was very excited and he didn't know what to do. He wore some water and put it in the water. Tim ate it all up with his mom and felt very lucky.

**temp_0.8, seed 1** (85 tokens, stop: eos)

> He saw a big rock. It was so black and scary. It was so big and soft! He bent down and grabbed his diary. He held his hands and made the foam out of the water. He was so happy and said thank you to his dad. After playing for his loyal, timmy's mom came so much. She gave him a hug and said, "I'm glad you had a great job."

**temp_0.8, seed 2** (150 tokens, stop: max_len)

> He saw a big surprise. It was a big box. It was a toy. He picked it up and ran to his mom. He picked up the scissors and put it in his mouth. He asked his dad to use it. Poor day, a little boy came to visit the park. He saw the old man and they wanted to make some cookies. They looked at the toy, but the boy was being angry. He started to cry, but he couldn't understand why. Suddenly, he saw a little girl with a big smile on her face. She grabbed the cheese and ran away. She ran towards it and looked at the pot. The little boy was so happy to have his toy design and gave timmy a hug. He was so

**temp_0.8, seed 3** (69 tokens, stop: eos)

> His mum started to be scared. But he knew he had to go to the park. He looked at the sky, waving the house, when he saw something shiny on the ground. He reached a trap and was so excited. He quickly jumped up and down and smiled and smiled. He had so much fun playing and playing with his friends.

**temp_0.8, seed 4** (150 tokens, stop: max_len)

> He was feeling tired. He wanted to be a great superhero when he arrived. Suddenly, he heard a loud noise. A kind man looked up at him and pointed at the old man. He was even more powerful and friendly. "Hey, why do you have the key?" he asked. "I love you too," said john. "You really steal the universe." john was scared and didn't know what to do. He held his mom's hand and said, "stop! That hurts! Your freeze surrender!" the bear was sad, but his dad sadly said, "please forgive me, I'll help you. You can have some ice cream!" and his mom smiled and said, "thank you, mommy

**temp_1.0, seed 0** (150 tokens, stop: max_len)

> He lay down and started his adventure. When he came back, he found a big sack that's hidden inside. He was so excited! He picked the jet in the mail and stepped out of the box. He looked around and found a big pot of spray ice - candles! Max bob wanted to make something special. He asked out, "you should be gentle when you pose it." the yacht smiled and thanked her. He skipped in the garden, the old ladder that was filled with colourful things. He was very pleased with the plants. When max saw the big building, he wore some water and put it in the box. Tim ate it really hard with his new sack and it made a happy sound. His mom was very pleased with

**temp_1.0, seed 1** (150 tokens, stop: max_len)

> He bent down to see what it was. He grabbed some energy all all around outside and tiptoed inside. But he did not listen and did not listen to the little boy's home. After playing - there, he heard a loud noise outside the tree. He caught it and said it was a deer. Ted saw so much that he noticed that he had broken his favourite shield. He began to cry, but the policeman didn't want to be free. Leo was fake very that he could do anything bad and wanted to give it back. He tried to catch the water. The monster created so much fun and he snipped it tight. He never pushed out of the lake for it and then thanked him for being so loyal. He never mentioned to leave

**temp_1.0, seed 2** (85 tokens, stop: eos)

> He saw a big surprise. It was a big prize. It looked interesting on the walls and day. When his walked was done, he smelled a rainbow. Tim was so excited! It was so big and impressive and he had lots of fun in a hut. He wanted to try it and see it again. He slowly stepped on the table, and soon he was a bit happier, but his leg would get dark.

**temp_1.0, seed 3** (102 tokens, stop: eos)

> His mum started to be scared in the air. Timmy was scared, but he did not want to break the things. He walked towards the old tree, but it was too far. He wouldn't find just because he needed his same hand. He kept signing until he found a ball in his boat. He made his friends itchy on the ground and he had a plan. His mum had made a nice decision with it. Luckily he had done a great thing that ever had done and could feel lonely again.

**temp_1.0, seed 4** (111 tokens, stop: eos)

> He was feeling tired. He wanted to be a great superhero his castle. So, he went to the store and found a rug. It was a big blue pastry. He picked it up and followed it around it. Inside, there were most amazing things to play with. Inside, he found a thick hedge. Tim was so happy and started eating the carrots in the snow. He wanted to climb on his boat now, so he added the hands to find it to go home. He couldn't believe that he had to freeze yet with his fingers.

**temp_1.2, seed 0** (142 tokens, stop: eos)

> He lay down and started his vacation back. He knew he had to put his paw on the grass. He touched the spring and croaked, but then something heard him. It was a big muscles with a fantastic ball wide in the grass. He couldn't believe what it had! Max bob wanted to give him warning. And he pushed the beans out. Daddy told the present to end the scarves at their town. Jay went to the bush, but there he wouldn't get scared. He would feel safe and sunny around his body. The boy sang up if they could play with the water and enjoy the sack before wearing his pan. At the safari, pat was very happy in his journey with the boat.

**temp_1.2, seed 1** (141 tokens, stop: eos)

> Mia bent down to see what it was. He grabbed some energy all all around outside and tiptoed inside. But he did and couldn't run very faster. The fog made the foam out and hit his tree! John heard her and startled him. He showed timmy how to twist the rock. Max was so grateful that so he wanted to not eat anything else. He mixed and tissues until his eyes slipped from his mouth. When the kid heard from him, leo was fake very surprised. He had never found somebody that he just cost. He liked to play with his cart. Taylor, mr memories, was happy and max wasn't allowed to play in such a loud brush he forgot and had thanked him.

**temp_1.2, seed 2** (85 tokens, stop: eos)

> Jimmy saw something strange. He was surrounded and he heard a puppy in the distance. He fell off and stopped his walked. He turned around and saw some children playing with questions for them. At the side, the other kids had shared of a special discovery. The man was having so much fun eating it in his yard, who was impressed because he was having fun chasing jane's toy, spinning juice and beat them everywhere.

**temp_1.2, seed 3** (150 tokens, stop: max_len)

> His mum started math. One year, he saw timmy stealing timmy who was in the garage. "Jake, why want to play with the aeroplane?" asked timmy. Tom laughed and said, "no just because you've worked hurt and mine!" tim was scared and did not know what boat was. Then, a fat on lightning, with another navy, worse, boys that arnold around. Jill and a group man walked down the hill. They saw beautiful object and honking and pellets. He couldn't believe at it, but he was so happy to see the sun run off. He drove medals to the garden. The boat was underground right! Jack was very excited! He ran and saw two animals and gather them motorcycles on the swings.

**temp_1.2, seed 4** (150 tokens, stop: max_len)

> She felt completely tired. Her john trotted from his window outside his castle and stopped that he gained an exciting seashell. It started to rain again when they started laughing. Lena cuddled into shrimp and had fallen even up powerful. Max's dad saw where the faucet were so fast. Inside was a sweet cold spot around - tim was wearing hands and laughing. "You really? What is that?" asked sue. "Glove is very interesting," he said. "I had never seen like a pastel warmer bottles." tim smiled and said to videos he liked rolling through the calm sea sadly in the wild line. He said goodbye and didn't forget to run around the track with his big go to sleep. Whenever they were pedaling arriving, lucy was

**topk_10, seed 0** (150 tokens, stop: max_len)

> He was very careful. His dad saw what he had been going to see. He thought he was funny and wanted to try new things. So, he asked his mom for help. His mom said, "I have an idea. Let's go and watch the water." max ran to the kitchen and put it in his pocket. Then, he took the big rock to his dad and he gave him a hug. Then he ate the yummy food he could do. But then, a gust of wind blew the ball into the clouds. He was scared! The rain was gone, and it hit the kite. The other ending made tim feel bad. His mom tried to fix it with her. She started to cry and cried. The rain

**topk_10, seed 1** (150 tokens, stop: max_len)

> He saw a big rock. It was so beautiful! He picked it up with a big smile on his face. He wanted to get the treasure, but the little boy wanted to be brave and he was so excited. He ran back outside and ran back to his room. He saw a boy selling the man. He asked him what was wrong, but he said it was too expensive. He had a surprise for his dad when he saw that he was looking for him. He asked him, "what can I go here and play with them?" the boy smiled. "Yes, we can do it together." the boy said, "yes, it would be fun and strong!" the little boy smiled and waved goodbye. From then

**topk_10, seed 2** (132 tokens, stop: eos)

> He saw a big hill. He decided to go home and find it. He looked out and saw something shiny in the grass. There he found a treasure. Tim was so excited! It was so big and scary! Suddenly, it was a big, round, green tree! Tim was so curious, he had never seen a big one. He was so excited! He took the ball out and ran around. He was so happy and grateful to the frog. He was able to get the pebble and put the banana in his pocket. From that day on, max always looked up to the clouds in the sky and all the animals in a safe place.

**topk_10, seed 3** (150 tokens, stop: max_len)

> His mum told him something that he needed to take. Tim was scared at first but he kept going and kept looking for more. When sam got to the store, he saw a man who was a boy. He said to him: "hi! What are you doing?" "yes, please." john was scared. He looked around and noticed that the old man was looking at the man who had a big bag on his face. He asked him what was wrong, and he explained to him something special. When the man was over, they found the puppy and it looked like a toy car. They both wanted the toy, but he was too young to have it. The boy and his dad played together together and had a wonderful time

**topk_10, seed 4** (82 tokens, stop: eos)

> He was feeling tired. He wanted to go home, but his friends told him that he could stay safe. His mom said, "it's okay, we need to go to the hospital." tim thought it was a great idea. He started to play with the water and his friends he found. He had a great time playing and laughing. He knew it was the best thing he could go on.

**topk_40, seed 0** (150 tokens, stop: max_len)

> He was very careful. His dad saw what made him feel guilty and asked him, "what's wrong?" tim smiled and said, "it's a magical, but it's very fragile. You don't have any things. Now we can use the ice to make it feel better." timmy was sad. He wanted so much fun, but his mom said, "it's ok, sam. You can't take it from my home." the old bear said, "I will just have a snack of them." tim didn't understand why the big brother ran away and wanted to play. But his mommy came running into the bathroom and said, "no, sam. You should not play outside. It is easy to go

**topk_40, seed 1** (121 tokens, stop: eos)

> He saw a big rock. It was so fast that it stopped all all around outside and saw a big, beautiful boat swimming in the sky. Suddenly tim heard a loud noise coming out from the sky. He looked around and saw a little boy. He was so excited to run fast and play. The man saw so much that he had a bit wet. He grabbed a ball and began to cry. His mom got angry and tried to catch him. The man was very surprised, but he knew he had to wait. After that, he learned that sometimes things can be harsh and listen to people.

**topk_40, seed 2** (150 tokens, stop: max_len)

> He saw a big hill. He jumped and ran after him, but he was just not a turn. When his mom was getting there, he noticed something strange! It was a big, scary bug. He wanted to find a little mouse. He tried to run away but he couldn't find it. He saw the rabbit who was standing in the park, looking happy to see what was happening. The rabbit was relieved. He started to panic, but he couldn't understand why. Suddenly, he heard a loud bark with his tail. The old frog was scared but still as he ran away, scared. The bug hopped away and ran away, but he remembered his mum was able to stay in the forest in a puddle. Then he remembered his

**topk_40, seed 3** (134 tokens, stop: eos)

> His mum started to be scared in the air. Timmy was scared, but he did not want to ignore his mom. He walked towards the old tree, and it slowly got closer. He reached a trap and was scared. His mom and dad came running and saw him and smiled. "Look, I'll get to a park on a slide with my dad," he said. "That's a bad idea," he told her. "Okay, but be careful. And don't worry," said his friend, "thank you for saving me." and it looked like a huge, scary animal. He was sure that his family was smiling too.

**topk_40, seed 4** (150 tokens, stop: max_len)

> He was feeling tired. He wanted to be a great superhero when he arrived. Suddenly, he had an idea. It started to rain again and he started to shake the big rock. Tim's mom opened his hand and saw that the rain were broken. He looked around. Inside was a big dog, "what's wrong?" lucy answered, "you had to be careful when we see it." tim tried again and he pushed the rock onto his head. His friend, dad, laughed and went back to his backyard. But then, he saw a big dog in the grass. He was playing with his ball all day long. Tim's mom made a sandwich with fun. Tim was very happy. The next day, tim went into

**topp_0.9, seed 0** (150 tokens, stop: max_len)

> He was very careful. His dad saw what he had written on his own and brought him to the door. Bob had a new picture of a big machine and he loved it. He thought about the perfect cookie he wanted to take the contest. When his mom took him to the airport, he was amazed by how amazing it was. He pointed the treasure and told the present what it was. He said he could catch it with it! He asked his mom, "can I mail some tools?" her mom thought of a moment and said, "yes, I can read your name and enjoy the organized treat. And only if you have a license to use your hair in it!" max thanked him and went to his garden. He found

**topp_0.9, seed 1** (122 tokens, stop: eos)

> He saw a big rock. It was so fast that it stopped all all around. The two teams stopped weeping and saw a big, bright waterfall. Tim looked around and saw a big tree with his tree! He wondered what was inside the garden. He asked his mom to buy it. Max was so happy that he took his kayak out of the water. He mixed it into a big field and put it back in the pile of places. He gave the bean a very beautiful melon with it. Jack and his friends laughed and cheered for the raft. They played together every day and enjoyed the weather together.

**topp_0.9, seed 2** (114 tokens, stop: eos)

> He saw a big surprise. It was a big box. It looked interesting than it had printed! Tom was scared, so he started to jump in it. When he came back, he saw a big, scary monster who had been poor. He tried to put the chair back on, but it was too late. He was so sad. He cried, but the boy took the pig out of the chimney. He was so happy and grateful to the bunny. From then on, the pony was careful when the jail flew down and it found them in the jungle.

**topp_0.9, seed 3** (129 tokens, stop: eos)

> His mum started to be scared. But he knew that he could borrow a haircut but he kept having hot words. When he woke up, he saw a big man in the distance. He was a lawyer and was walking to his house. He was sad and curious. As the days was getting closer, tim saw that it was on a puppy with a loud noise. He couldn't believe it. He tried to run away, but the sock got scared. The monster had woken and jimmy got stuck on his garden. He thought he was so nice and he made the sun run away. He was glad he never caught the clouds again again.

**topp_0.9, seed 4** (107 tokens, stop: eos)

> He was feeling tired. He wanted to be a great superhero when he arrived. Suddenly, he heard a loud noise outside. He saw a big man standing in the lake. He was amazed by the shrimp in the air and that he liked looking very fast. Tim went out and found a big dog. The puppy was excited to meet it. He decided to try to balance it in his pocket. He remembered what the man had led, but he became very safe. He was happy to be safe and stay safe in his backyard.

**topk_40_rep1.2, seed 0** (105 tokens, stop: eos)

> His mom saw him holding his finger and gave him a big hug. One night, joey's mom asked him a question from his bedroom. Bob felt excited and wanted to try it with him. After a bath, timmy was ready for the bus to ride and play in the park. Bob wanted to make something special. And his mommy said no, and she told the storekeeper to always find something useful for him before eating them. Lily was so happy that he could keep her new bag when a few days later by himself.

**topk_40_rep1.2, seed 1** (117 tokens, stop: eos)

> Mia saw a big rock. It was so fast that she stopped playing with her big legs but then she stopped moving. Max ran towards the slide and tried to get him harder. Suddenly, the boy heard a voice. "Hey! Come here!" tim cried, but she thought it sounded fun. She started to cry. Tom noticed that his dad had been coming by. She walked over the gate with the red glass in the air and gave him the balloon. She was so happy, with jack and she continued exploring and enjoying the rest of the moment for a few time.

**topk_40_rep1.2, seed 2** (135 tokens, stop: eos)

> Jimmy saw a big hill and decided to run around with him. It looked so yummy! After a while, his friend sam stopped at a nearby pond. Tim wanted to climb it with it at hiding. He thought about what to go and asked if he could put the red stone beside them. Max said goodbye, then slowly stepped into the grass. As soon as the boy took them, she felt even more careful when her mom started working up up to the hill. Soon, it was time for max to rest in the water. It was so dark and strong. Mia's dad picked out his shoes and took it home. They ran to spot and played happily happily.

**topk_40_rep1.2, seed 3** (150 tokens, stop: max_len)

> His mum started to be scared in. So she got her flute tightly and they both jumped on the table. Suddenly, a gentle wind blew from him from behind it a rock! Timmy looked around and saw a big, shiny puppy near the tree. He was curious, and decided to walk down the street. John was scared at first, but then he had an idea. He jumped up and down and tried a snowball out of his mouth with its hands. The monster had a lot of energy. He asked the dog why the dove was so nice they did it, and it looked like he was waiting for him. He said, "hi frog! Can you help me get out of this lake?" the pig smiled and said, "don

**topk_40_rep1.2, seed 4** (150 tokens, stop: max_len)

> She felt sad as she ran to the kitchen and put her hand in his mouth. As she had closer to him it a big dog appeared! They walked around the lake until there were different trees. Suddenly, it turned into its wings, looking for food to play with. Jane was scared, but then she heard a loud noise from behind the side of her house. It was a giant clown standing on a boat in uniforms - he couldn't have taken off to explore, just like how scary he could find. The puppy smiled and said to lily, "hi max. Give you his collar! What's wrong?" sam got angry and wagged his tail against the bark and jumped up and down at a big dog. "Hey - dog!
