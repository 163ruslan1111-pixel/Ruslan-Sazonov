# Видеопромпт: анатомия, скелет, пример

Содержание: 1. Порядок блоков · 2. Что писать в каждом блоке · 3. Скелет · 4. Пример G1 · 5. Адаптация под платформу

## 1. Порядок блоков

Один текст, сверху вниз:

1. REFERENCES — что на каждой приложенной картинке
2. Персонажи — лок внешности + характер
3. CAST — сколько людей, кто где, массовка, расстановка
4. STATES — старт и цель, если мир меняется
5. THE RULE — одна невозможная вещь
6. CONTINUITY — что не меняется
7. PERFORMANCE — живая неподвижность, манеры
8. SPEECH — язык, темп, начало речи
9. REALISM OF MOVEMENT — только при физическом воздействии
10. LIGHT — свет вместо слова cinematic
11. STYLE — камера и звук
12. SHOT-блоки — таймкоды, CAMERA / ACTION / DIALOGUE / SOUND
13. ENDPOINT — жёсткий конец
14. SEAM OUT / SEAM IN — стыки с соседними частями
15. NEGATIVE — одним списком в конце или в отдельное поле платформы

Длительность, формат, разрешение и звук ставятся в интерфейсе платформы. В тексте промпта их нет.

## 2. Что писать в каждом блоке

### REFERENCES
`@NAME = reference image N. <что на картинке и зачем она>`
- Номер = порядок загрузки файлов. Перепутал порядок — персонажи поменяются лицами.
- Описание работает как бриф: детали из него доезжают до кадра (часы, фактура стены, вывеска).
- Если платформа использует свои теги (@Image1, [image 1] и т. п.) — ставь их вместо «reference image N», описания оставляй: они страхуют привязку.
- На практике надёжно держится до 5 референсов; больше работает, но привязка слабеет. Приоритет: лица → одежда → локация-старт → локация-цель → предметы.

### Персонажи
Лок:
`@NAME — locked reference: face, hair and clothing are read from reference image N and from nowhere else. Clothing: [полный именной список]. Nothing added, nothing removed. Do not re-describe his face.`
- Полный список одежды — это указатели на референс. Неполный — модель дорисует своё.
- Лицо словами не описываешь: описание спорит с картинкой, и лицо плывёт.
- Характер — 2–3 строки поведения: как двигается, как говорит, чем заняты руки, от чего проигрывает. Без этого персонаж превращается в функцию, которая произносит реплики.
- Снятая вещь (очки, часы, пиджак) остаётся снятой во всех следующих частях: пиши это явно и добавляй негатив на возврат.
- Кого нет в этой генерации, не упоминай нигде, даже в негативе: длинный запрет делает его главным героем сцены.
- Имена известных персонажей и актёров не пиши — сработает фильтр прав.

### CAST
- Точное число людей; кто где — через предметы комнаты («by the window», «at the far end of the counter»), а не left/right.
- Двое стоящих: `STAGING — never a frontal lineup: a triangle, the camera about thirty degrees off the axis between them.`
- Массовка — список с населённого плейта слово в слово: `A — [age, clothing, exact place, looping action]; B — …; each is present in the first and the last frame, nobody enters, exits or is replaced; nobody looks at the camera.` Хотя бы один в глубине всегда идёт.

### STATES — если мир меняется
`@STATE1 is the scene at the START: … @STATE2 is the TARGET by t=X s: … Match @STATE2 exactly, everything else identical. The camera does not move while the state changes.`

### THE RULE
`THE RULE — the one impossible thing in this film: [механика одной фразой]. [Физика: твёрдые тела на заданной траектории, таймкоды, конечное состояние; кто замечает, кто нет.] Everything else is ordinary documentary footage.`
- Трансформация: `between one frame and the next — not a fade, not a dissolve, not a morph`; `one single object mid-change in every frame, never a cut, never a crossfade, never a swap`.
- Перенос предмета: `carried by X, never floating`.
- Свет: целевой плейт + `overall brightness never decreases`, иначе свет уйдёт в сумерки.

### CONTINUITY
Геометрия, позиции, свет, лица, одежда, предметы, направление движения по экрану. Что снято — то снято.

### PERFORMANCE
`living stillness — visible breathing, natural blinks, micro weight shifts; nobody frozen; the listener is always busy with a small action.` + личные локи.
- Жест — амплитудой и временем возврата: `two fingers flick a hand's width at hip height, back at rest in half a second`. Не направлением — иначе рука-семафор.
- Предмет в руке: `prop and hand are one object`.

### SPEECH
`SPEECH — [language], spoken with natural [language] stress; all dialogue is generated in this video. Speech begins on the FIRST FRAME, no silent lead-in. Unhurried, never gabbled. Accent by a pause before the word, never by volume.`
- У каждой реплики владелец: `ONLY @X SPEAKS. @Y's mouth stays closed.` Перед важной репликой камера показывает говорящего.
- Голос из телефона или за кадром так и называй: `a man's voice from the phone speaker`.
- Реплики — обычным текстом в «кавычках», без ударений заглавными буквами и без транскрипции.

### REALISM OF MOVEMENT — при физическом воздействии
Сила + список предметов, на которые она действует; тело — обычный шаг: `full natural stride, heel first, arms swinging, head level, normal speed`. Потолок словами: `a real person walking into a strong headwind leans about five degrees and simply walks heavier`. Контраст в одном кадре: на него действует — на соседа нет.

### LIGHT
Источник, направление, характер, контраст, палитра (основной / вторичный / акцент). Этот абзац заменяет слово cinematic.

### STYLE — база, адаптируй под ролик
`believable documentary camera, real lens behaviour, natural handheld micro-movement, practical light only. No colour-grading gloss. No slow motion. No music. Sound accents on camera pushes, cuts and impacts are welcome.`

### SHOT-блоки
```
SHOT 1 — 0–4 s
CAMERA: крупность, ракурс, движение (или locked на смене мира)
ACTION: физика с конечными состояниями и таймкодами
DIALOGUE: ONLY @X SPEAKS: «реплика»
SOUND: что звучит + акцент на движение камеры / рез / удар
```
- Таймкоды целыми секундами, без дыр и наложений, сумма = длительность генерации.
- Реплика может переходить через рез.
- Короткие планы модель растягивает: помечай brief и держи жёсткие таймкоды.

### ENDPOINT
`ENDPOINT: hard end at N s on [последний слог / событие]. No dead time, no empty tail.`

### SEAM OUT / SEAM IN
`SEAM OUT: [крупность + субъект последнего кадра]. SEAM IN: [крупность + субъект первого кадра] — differs from the previous part's last frame in BOTH shot size and subject.`
У первой части — только SEAM OUT, у последней — только SEAM IN.

### NEGATIVE
Собирай из того, что реально может сломаться в этой сцене:
- люди: frozen people, mannequin stillness, waxwork poses, motionless listener, identity drift, a different face, the other man's clothing on him
- массовка: frozen background people, motionless extras, posed group, everyone facing camera, duplicated faces, cloned people
- двое в кадре: frontal lineup, both facing the camera in a row
- жесты: outstretched arm, semaphore pose, T-pose, gesture held
- физика: crouching, bending double, exaggerated lean, contorted posture, gliding, sliding without steps, feet not touching the floor, floating, rubbery limbs, video-game animation
- камера: time-lapse, slow motion, speed ramp, orbit, drone, camera travelling out of the room
- свет, если не меняется: dusk, twilight, exposure dropping
- прочее: music, subtitles, captions, watermark, dead time, empty tail, silent gaps with no ambient sound

Не пиши в негатив:
- «no text» — не работает, модель всё равно рисует мусорные буквы;
- персонажей, которых нет в кадре;
- greyscale, monochrome, black and white — красят одежду даже из негатива;
- кучу насильственных слов — фильтр считает их и в негативе.

## 3. Скелет

```
REFERENCES: @HERO = reference image 1, character sheet: face, hair and every item of his clothing. @LOC = reference image 2, [location, camera side, key objects, light]. [@STATE2 = reference image 3, the same place at the TARGET state: what changed.] [@PROP = reference image 4, ...]

@HERO — locked reference: face, hair and clothing are read from reference image 1 and from nowhere else. Clothing: [full named list]. Nothing added, nothing removed. Do not re-describe his face.
CHARACTER @HERO: [2–3 lines of behaviour].

CAST: exactly [N] people — [who, where, by room landmarks]. [STAGING ...] [Background cast, word for word from the plate: A — ...; B — ...; each present in the first and the last frame, own small loop, nobody enters, exits or is replaced, nobody looks at the camera.]

[@LOC is the scene at the START: ... @STATE2 is the TARGET by t=X s: ... Match @STATE2 exactly, everything else identical. The camera does not move while the state changes.]

THE RULE — the one impossible thing in this film: [...]. Everything else is ordinary documentary footage.

CONTINUITY: [...]

PERFORMANCE: living stillness — visible breathing, natural blinks, micro weight shifts; nobody frozen; the listener is always busy with a small action. [personal locks]

SPEECH — [language], spoken with natural [language] stress; all dialogue is generated in this video. Speech begins on the first frame. Unhurried, never gabbled.

[REALISM OF MOVEMENT: ...]

LIGHT: [...]

STYLE: believable documentary camera, real lens behaviour, natural handheld micro-movement, practical light only. No colour-grading gloss. No slow motion. No music. Sound accents on camera pushes, cuts and impacts are welcome.

SHOT 1 — 0–4 s
CAMERA: ...
ACTION: ...
DIALOGUE: ONLY @HERO SPEAKS: «...»
SOUND: ...

SHOT 2 — 4–8 s
...

ENDPOINT: hard end at [N] s on [...]. No dead time, no empty tail.
SEAM OUT: [...]. SEAM IN: [...].

NEGATIVE: [...]
```

Квадратные скобки — только для тебя. В промпте, который получает пользователь, их нет.

## 4. Пример — G1, 12 с

Идея: квартира. Парень собирается в зал, а невидимая сила тянет к дивану — только его и его вещи. Сосед ничего не замечает. На примере видно: одно невозможное, сила через предметы, контраст в одном кадре, три слоя глубины, речь с первого кадра, звуковые акценты, стык.

`G1 · 12 с · 16:9 · звук вкл. · референсы по порядку: 1 — лист Макса, 2 — лист Дэна, 3 — мастер-плейт квартиры`

```
REFERENCES: @MAX = reference image 1, character sheet of the first man: face, hair and every item of his clothing. @DAN = reference image 2, character sheet of the second man: face, hair and every item of his clothing. @FLAT = reference image 3, a small lived-in apartment photographed from the kitchen side: open kitchen counter in the foreground, a grey fabric couch against the far wall under the window, the front door in the right wall with a small key shelf beside it, warm afternoon daylight.

@MAX — locked reference: face, hair and clothing are read from reference image 1 and from nowhere else. Clothing: black zip hoodie with white drawstrings, grey joggers, white running shoes. Nothing added, nothing removed. Do not re-describe his face.
CHARACTER @MAX: easy-going and a little guilty; keeps moving as if nothing is happening, answers without looking up.

@DAN — locked reference: face, hair and clothing are read from reference image 2 and from nowhere else. Clothing: olive T-shirt, navy canvas apron, dark jeans, grey socks. Nothing added, nothing removed. Do not re-describe his face.
CHARACTER @DAN: dry and unhurried, busy with food, looks up only when he speaks.

CAST: exactly two people — @DAN behind the kitchen counter in the foreground, @MAX between the couch and the front door. Nobody else.

THE RULE — the one impossible thing in this film: an invisible pull toward the grey couch acts ONLY on @MAX and on his own things — his clothes, his keys, his water bottle. It is shown by objects, never by his body: drawstrings and shoelaces lean toward the couch, the water surface in his bottle tilts toward it, his keys slide toward it. @DAN and everything around him stay untouched: his apron strings hang straight, the bread crumbs stay put. Nobody comments on the pull. Everything else is ordinary documentary footage.

CONTINUITY: couch, window, door and key shelf keep their places in every shot; the afternoon light does not change; a clear plastic water bottle, half full, cap off, stands on the floor by the door in shot 1 and is in @MAX's left hand in shot 3.

PERFORMANCE: living stillness — visible breathing, natural blinks, micro weight shifts; nobody frozen. @DAN slices bread in short strokes the whole time; the bread knife and his hand are one object.

SPEECH — Russian, spoken with natural Russian stress; all dialogue is generated in this video. Speech begins on the first frame. Unhurried, never gabbled.

REALISM OF MOVEMENT: @MAX walks with a full natural stride, heel first, arms swinging, head level, a little slower than normal; a real person walking against a pull leans at most five degrees and simply walks heavier. The force lives in the objects listed in THE RULE, never in his posture.

LIGHT: warm low sun through the window behind the couch, soft bounce from white walls, gentle contrast; palette warm grey and oak, the white drawstrings as the accent.

STYLE: believable documentary camera, real lens behaviour, natural handheld micro-movement, practical light only. No colour-grading gloss. No slow motion. No music. Sound accents on camera pushes, cuts and impacts are welcome.

SHOT 1 — 0–4 s
CAMERA: medium shot over @DAN's shoulder, his knife hand soft in the foreground; @MAX sharp in the middle ground by the door, the couch behind him.
ACTION: @MAX ties his left shoe; both laces and the hoodie drawstrings stretch sideways toward the couch and stay stretched; the water surface in the bottle at his feet is tilted toward the couch. @DAN slices bread, his apron strings hanging straight.
DIALOGUE: ONLY @DAN SPEAKS, @MAX's mouth stays closed: «ты же в зал собирался». Then ONLY @MAX SPEAKS, without looking up: «да иду я, иду».
SOUND: knife on the board, a shoelace snap, a low hum coming from the couch side.

SHOT 2 — 4–7 s
CAMERA: close-up of the key shelf by the door, a quick push-in as his hand enters the frame.
ACTION: @MAX's right hand reaches for the keys; the keys slide across the shelf away from his fingers toward the couch side and stop at the edge; he catches them on the second try.
SOUND: a metal scrape along the shelf, a soft hit on the push-in.

SHOT 3 — 7–12 s
CAMERA: wide shot from the kitchen side, @DAN's bread board soft in the foreground, @MAX in the middle ground, the couch and the window in the background.
ACTION: @MAX, the bottle in his left hand, walks to the door with heavy normal steps; the water in the open bottle tilts back toward the couch and a few drops fly backward past his hip; at 11 s his hand closes on the door handle.
SOUND: steps on laminate, water slosh, the handle click on the last frame.

ENDPOINT: hard end at 12 s on the handle click. No dead time, no empty tail.
SEAM OUT: wide shot, @MAX at the door.

NEGATIVE: crouching, bending double, exaggerated lean, contorted posture, gliding, sliding without steps, feet not touching the floor, objects floating with no cause, the pull affecting @DAN or his things, frozen people, mannequin stillness, identity drift, the other man's clothing on him, frontal lineup, time-lapse, slow motion, orbit, drone, music, subtitles, captions, watermark, dead time, empty tail.
```

Риск: ключи не поедут или поедут не туда. Рычаг: одна строка — «the keys slide 20 cm toward the couch side, a rigid solid object on a straight path».
Проверить: шнурки и завязки капюшона тянутся к дивану; вода в бутылке наклонена к дивану; фартук Дэна висит ровно; реплики сказаны нужными ртами.

Следующая часть (G2) открывается другой крупностью и другим субъектом — например, крупным планом Дэна или дивана.

## 5. Адаптация под платформу

- Есть отдельное поле негатива — переноси NEGATIVE туда.
- Модель не понимает негатив — главные пункты переводи в утверждения внутри текста («his posture stays upright» вместо «no bending»), остальное убери.
- Выключи «улучшение промпта» (prompt enhance, magic prompt), если платформа его предлагает: оно переписывает структуру. Подставляет свой пресет или стиль вместо промпта — откажись; слово, совпавшее с названием пресета, замени синонимом.
- Лимит длины промпта — сокращай по порядку: STYLE до одной строки → LIGHT до одной строки → повторы в NEGATIVE → общие фразы PERFORMANCE. Не трогай REFERENCES, THE RULE, реплики, таймкоды и SOUND-акценты.
- Короткий потолок клипа (5–8 с) — 1–2 плана на генерацию, генераций больше, стыки по тем же правилам.
- Нет родного звука — убери SPEECH и SOUND, оставь таймкоды реплик для липсинка; звук собирается на монтаже.
- Только стартовый кадр (image-to-video без референсов) — стартовый кадр = плейт нужного состояния с персонажем в позиции первого кадра; блок REFERENCES не нужен, остальное без изменений.
- Длинный потолок (20–30 с) — не повод растягивать: длину решает число событий, а сложный непрерывный план всё равно держится ~6 с.
