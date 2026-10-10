# Серия 1 · Кадры и видео · К1–К5 (кухня Громовых)

Утверждённые референсы: kitchen-1985 · hozyayushka-1985 · petr-1985 · nadya-1985 · misha-1985 · lemonade · coupon.

Порядок для каждого куска:
1. **Nano Banana** — новый чат, приложить картинки в указанном порядке, вставить промпт кадра → получить стартовый кадр.
2. **Kling 2.5** — режим «Image to Video», загрузить стартовый кадр, вставить видеопромпт, выставить длительность. Негатив — в поле Negative Prompt, если оно есть. «Улучшение промпта» (enhance) выключить.
3. Звука в Kling нет: голоса и шумы добавлю на монтаже, губы подгоним Lip Sync.

Правка сценария: Надя поправляет Мише пионерский галстук (на листе у него галстук, а не бант). К4 разбит на два куска — у Lip Sync одно лицо на кусок надёжнее.

---

## К1 · 5 с · лимонад

**Кадр (Nano Banana)** — приложить: @image1 — lemonade, @image2 — hozyayushka-1985, @image3 — misha-1985
```
Create one film still, horizontal 16:9, 35 mm film photograph look, Kodak Portra colours, fine grain, photorealistic.
@image1 is the glowing green lemonade bottle on the yellow checkered oilcloth — keep the bottle and its label exactly as in @image1.
@image2 is the robot: only its chrome three-finger gripper is in frame, entering from the left, holding a small steel bottle opener hooked under the crimped cap of the bottle, which is now closed.
@image3 is the boy: only his small hand and the white short sleeve of his shirt enter from the right, fingers reaching toward the bottle; behind the bottle his face is soft and out of focus, red garrison cap, eyes on the bottle.
Close-up at table height, 50 mm lens, morning sun from the window behind, condensation on the glass.
No other text, no watermark.
```

**Видео (Kling)** — `К1 · 5 с · 16:9 · старт: кадр К1`
```
Close-up at table height in a sunny 1985 Soviet kitchen. Locked camera with slight natural handheld micro-movement, real lens behaviour, 35 mm film look.
SHOT 1 — 0–2 s: the robot's chrome gripper levers the bottle opener; the metal cap pops off and flips away out of frame; a puff of fine mist rises from the neck.
SHOT 2 — 2–5 s: the green lemonade glows a little brighter from inside, a column of tiny bubbles rushes up; the boy's small hand closes around the wet bottle and pulls it out of frame toward himself; the gripper withdraws to the left.
The glow is soft and steady, never flickering, never sparks. The label stays sharp and unchanged.
ENDPOINT: hard end at 5 s as the bottle leaves the frame.
```
Негатив: `flickering light, sparks, explosion, liquid spilling, extra hands, extra fingers, deformed hand, label changing, text morphing, slow motion, time-lapse, music, subtitles, watermark`

Риск: рука ребёнка или клешня «плывут». Рычаг: убрать клешню из кадра, крышка уже снята — остаётся только рука и свечение.
Проверить: этикетка не поменялась, у ребёнка пять пальцев, свечение не мигает.

---

## К3 · 10 с · Хозяюшка и блин

**Кадр (Nano Banana)** — приложить: @image1 — kitchen-1985, @image2 — hozyayushka-1985, @image3 — misha-1985, @image4 — lemonade
```
Create one film still, horizontal 16:9, 35 mm film photograph look, photorealistic. The same kitchen as @image1 — same tiles, refrigerator with the smiling boy magnet, yellow oilcloth table, window with the spire, TV on the bracket, stove, samovar. Camera at 120 cm, 35 mm lens, from the refrigerator side, looking at the stove and the end of the table.
The robot from @image2, exactly the same design and the same folk-pattern apron, stands at the gas stove holding the cast-iron frying pan with a thin pancake in it.
The boy from @image3, exactly the same face and clothing, sits at the table end nearest the stove, holding the glowing green bottle from @image4 in both hands, a thin green lemonade moustache on his upper lip, grinning.
Morning sun from the window, warm soft shadows. Nobody looks at the camera. No text, no watermark.
```

**Видео (Kling)** — `К3 · 10 с · 16:9 · старт: кадр К3`
```
Sunny 1985 Soviet kitchen, believable documentary camera, natural handheld micro-movement, 35 mm film look, warm morning window light. No slow motion.
The robot moves on its single wheel smoothly, arms jointed and mechanical, its round amber lamp eyes glowing steadily. The boy is alive the whole time: breathing, blinking, swinging his legs.
SHOT 1 — 0–4 s: medium shot. The robot flicks the pan; the thin pancake flips once in the air about 30 cm high and lands flat back in the pan. The boy laughs and claps once.
SHOT 2 — 4–10 s: the robot sets the pan on the stove, rolls half a metre to the boy and, holding a white cloth napkin in its gripper, gently wipes the green moustache from his upper lip while talking: the chrome speaker grille on its face lights up softly in rhythm with the words. The boy wrinkles his nose, giggles and pulls the bottle closer to his chest.
CONTINUITY: kitchen layout, light and the apron pattern stay identical; the bottle stays in the boy's hands.
ENDPOINT: hard end at 10 s as the napkin leaves his face.
```
Негатив: `robot walking on legs, extra arms, robot face changing, pancake duplicating, pancake sticking to ceiling, boy frozen, mannequin stillness, identity drift, different child, slow motion, time-lapse, music, subtitles, watermark`

Риск: блин в воздухе — модели плохо держат подброс. Рычаг: заменить на «the robot slides the finished pancake from the pan onto the stack on a plate».
Проверить: у робота одно колесо и две руки, лицо мальчика как на листе, фартук не изменился.

---

## К4a · 5 с · Пётр

**Кадр (Nano Banana)** — приложить: @image1 — kitchen-1985, @image2 — petr-1985
```
Create one film still, horizontal 16:9, 35 mm film photograph look, photorealistic. The same kitchen as @image1. Medium shot, 50 mm lens, camera at eye level near the stove, looking toward the window: the lace curtains and the city with the spire and the airship behind him, slightly overexposed.
The man from @image2, exactly the same face, hair and clothing — light grey suit, white shirt, narrow red tie, red satin ribbon bow on the left lapel, steel wristwatch — stands by the window, three-quarter to the camera, finishing knotting his red tie with both hands, glancing down at his wristwatch.
Warm morning backlight from the window, soft fill. Nobody looks at the camera. No text, no watermark.
```

**Видео (Kling)** — `К4a · 5 с · 16:9 · старт: кадр К4a`
```
Medium shot by the kitchen window, 1985, believable documentary camera, natural handheld micro-movement, 35 mm film look, warm backlight.
SHOT 1 — 0–5 s: the man pulls the knot of his red tie tight, flicks his wrist to look at his watch, then turns his head toward the room and says a short hurried sentence with a smile, natural mouth movement. He keeps breathing and blinking; the lace curtain behind him moves slightly in the breeze.
His face stays clearly visible, turned three-quarter toward the camera.
ENDPOINT: hard end at 5 s as he finishes speaking.
```
Негатив: `face turning away, face hidden by hands, identity drift, different face, tie changing colour, ribbon bow disappearing, frozen, mannequin stillness, slow motion, music, subtitles, watermark`

Реплика для озвучки (ElevenLabs, голос Петра): «Опаздываем! Парад в десять.»

---

## К4b · 5 с · Надя и Миша

**Кадр (Nano Banana)** — приложить: @image1 — kitchen-1985, @image2 — nadya-1985, @image3 — misha-1985
```
Create one film still, horizontal 16:9, 35 mm film photograph look, photorealistic. The same kitchen as @image1, by the cream refrigerator with the smiling boy magnet. Medium shot, 40 mm lens, eye level of a kneeling adult.
The woman from @image2, exactly the same face, hair and clothing — navy polka-dot dress with white round collar, red carnation — kneels on one knee in front of the boy, both hands straightening the knot of his red pioneer neckerchief.
The boy from @image3, exactly the same face and clothing — red garrison cap, white shirt, red neckerchief, navy shorts, white knee socks — stands facing her, chin raised, impatient.
Camera about thirty degrees off the axis between them, both faces visible. Morning sun from the window. Nobody looks at the camera. No text, no watermark.
```

**Видео (Kling)** — `К4b · 5 с · 16:9 · старт: кадр К4b`
```
Medium shot in a sunny 1985 kitchen by the refrigerator, believable documentary camera, natural handheld micro-movement, 35 mm film look.
SHOT 1 — 0–5 s: the kneeling woman tugs the boy's red neckerchief knot straight, smooths its ends with both hands, then looks up past the camera toward someone across the room and says a short teasing sentence with a warm smile, natural mouth movement. The boy fidgets, shifts from foot to foot, adjusts his garrison cap.
Both keep breathing and blinking; her face stays clearly visible.
ENDPOINT: hard end at 5 s as she finishes speaking.
```
Негатив: `boy speaking, extra hands, deformed fingers, neckerchief changing, identity drift, different face, frozen, mannequin stillness, slow motion, music, subtitles, watermark`

Реплика для озвучки (голос Нади): «Без тебя не начнут, инженер.»

---

## К5 · 5 с · талон на холодильнике

**Кадр:** готовая картинка coupon (утверждённая, со звездой) — без Nano Banana.

**Видео (Kling)** — `К5 · 5 с · 16:9 · старт: coupon`
```
Close-up of a pink paper card held by a purple magnet on the door of a cream refrigerator, 1985 kitchen, 35 mm film look.
SHOT 1 — 0–5 s: a very slow, steady push-in toward the card. Halfway through, a soft moving shadow of someone passing between the window and the refrigerator slides across the door and the card, then the warm sunlight returns. The paper edge flutters very slightly in a breeze.
The typed text and the stamp stay perfectly sharp and unchanged in every frame.
ENDPOINT: hard end at 5 s.
```
Негатив: `text changing, letters morphing, new text, card moving, magnet moving, camera shake, slow motion, music, subtitles, watermark`

Риск: Kling «перепишет» буквы. Рычаг: убрать наезд камеры — статичный кадр держит текст надёжнее; в крайнем случае наложу оригинальную картинку на монтаже.

---

## К2 · реклама с Атомкой — позже

Нужен отдельный лист талисмана Пионер Атомка (рисованный ретро-мультик). Сделаем следующей партией вместе с парадом.
