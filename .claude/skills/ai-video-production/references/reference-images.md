# Референсы и плейты

Модель не помнит прошлую генерацию. Всё, что должно совпасть в двух генерациях, совпадёт, только если в обе приложена одна и та же картинка.

## 1. Список — до первого видеопромпта

Пройди карту генераций и выпиши: персонажи · костюмы, если меняются · локации и их состояния · планы с другой точки · предметы, которые видны в двух генерациях и больше · надписи, которые должны читаться · массовка · рассадка за столом.
Эпизодическое, что видно один раз, референса не требует.

## 2. Типы референсов

1. **Лист персонажа** — из 2–3 фото реального человека или из описания. Четыре вида на одном листе: фронт в рост, спина в рост, три четверти в шаге, по пояс с предметом. Одна одежда и один свет на всех видах. Один лист держит и лицо, и одежду.
2. **Мастер-плейт локации** — один на локацию. Камера описана физически: высота от пола в сантиметрах, фокусное, угол к стене. Три слоя глубины.
3. **Населённый плейт** — тот же интерьер с фиксированным составом людей по буквам. Он и есть референс для общих и средних планов. Пустой плейт — только для крупных планов, где людей нет или в расфокусе максимум один.
4. **Состояния** — правкой мастера, а не новой генерацией: предмет появился, исчез, постарел, вода поднялась, свет выключен. Каждое изменение мира — пара СТАРТ + ЦЕЛЬ.
5. **Крупности и обратные точки** — тоже правкой мастера с приложенным мастером, иначе мебель и свет поедут. Общие и средние планы в видео снимаются с той же стороны, что и плейт.
6. **Предметы** — отдельной картинкой, если предмет виден дважды. Продукт клиента — только с его реального фото.
7. **Надписи** — плейт с текстом (вывеска, стойка, штамп); текст продиктован по буквам — и здесь, и в видеопромпте.
8. **Рассадка** — если за столом несколько человек: плейт комнаты, где все уже сидят. Места описываются ориентирами комнаты («у окна», «у двери»), не «слева/справа». Без этого между резами люди меняются стульями.

## 3. Правила

- Формат картинки = формат видео.
- Только цветные референсы; слов greyscale, monochrome, black and white нет нигде — даже в негативе они обесцвечивают одежду.
- Один референс — одна роль. Референс сильнее описания.
- Плейт «сфотографирован как реальное место»: документальное фото, износ, мелкие несовершенства, эталон масштаба в кадре.
- Экраны телефонов и мониторов — пустые или чистый хромакейный зелёный; содержимое экрана ставится на монтаже.
- К каждому референсу — короткое описание (до ~180 символов, у персонажа первым идёт возраст). Оно пойдёт в блок REFERENCES видеопромпта.

## 4. Каким генератором

Любым, который умеет редактировать картинку по приложенной — для цепочки состояний это обязательно. Если редактирования нет, генерируй состояние с приложенным мастером как референсом и повторяй в промпте всю опорную геометрию.

## 5. Шаблоны

### Мастер-плейт
```
Documentary photograph, location plate for film production, [horizontal 16:9 / vertical 9:16] framing.
CAMERA: [height in cm from the floor], [focal length] lens, [angle to the main wall], [what is in the centre of the frame].
SCENE: [layout left to right, every key object]; three depth layers — [object close to the lens] / [the scene] / [background].
DETAILS: [wear, marks, small imperfections, one object that shows the scale].
LIGHT: [source, direction, time of day].
CONSTRAINTS: no people, no watermark, no glamorization, no readable text or logos unless listed above; photographed as a real place, no rendering look.
```

### Населённый плейт
Тот же промпт, вместо «no people»:
```
PEOPLE, nobody looks at the camera: A — [age, clothing, exact place, what he is doing]; B — [...]; C — [...].
```
Этот список потом слово в слово идёт в каждую видеогенерацию с этой локацией.

### Состояние — правка мастера, мастер приложен
```
Edit this image.
CHANGE: [only what changes, concretely].
PRESERVE, exactly as in the source: camera angle, framing and lens feel; [full list of the key geometry and objects — repeat it in full on every edit].
CRITICAL — camera-locked plate: overlaying this image on the source must align perfectly. Do not move the camera closer. Do not enlarge objects.
REALISM: the new element sits in the existing light, no sticker effect.
Constraints: change only the above.
```
«Свет выключили днём» пиши явно: выключен практический свет, небо за окном остаётся таким же ярким.

### Крупнее или с обратной точки — правка мастера
```
Edit this image.
CHANGE: move to a tighter framing of [what] from the same side of the room, [focal length] lens.
PRESERVE: the same room, furniture, materials, light direction and colour; [key objects that must stay in frame].
Constraints: nothing new added to the room.
```

### Лист персонажа — 2–3 фото приложены
```
Character reference sheet for film production, one sheet, four panels on a plain light grey background, the SAME person in all four panels, the SAME clothing and the SAME light in every panel: panel 1 full-height front view standing relaxed; panel 2 full-height back view; panel 3 three-quarter view mid-step; panel 4 waist-up holding [prop]. Face, hair and build exactly from the attached photographs. Wardrobe: [full named list]. No text, no labels, no watermark.
```
Персонаж придуманный — вместо «exactly from the attached photographs» опиши возраст, тип лица, причёску, телосложение. Дальше лист становится референсом, и описание лица из видеопромптов уходит.
Лист из двух видов модель иногда читает как двух людей — пиши «TWO VIEWS OF THE SAME PERSON».

### Надпись
```
[Object] with the text "OPEN LATE" in [font style, colour, size relative to the object], spelled exactly O-P-E-N L-A-T-E, sharp and fully readable, [material]. [The rest of the plate as usual.]
```

### Раскадровка — по желанию
```
Storyboard sheet, twelve panels in a 4×3 grid, graphite pencil on white paper, loose hand-drawn hatching, no colour. The same characters in every panel where they appear, from the attached references. Panel 1: [what, shot size]. ... Panel 12: [...]. Each panel is a frozen instant inside motion, not a pose. No dialogue text, no captions.
```
Если лист прикладывается к видеомодели как план, в видеопромпт добавь: «the sheet is a shot plan, not a picture; cells read left to right, top to bottom; never render the grid, gutters, labels or numbers; never a split screen».

## 6. Проверка до видео

- Лицо и одежда совпадают на всех видах листа.
- Состав массовки один и тот же на всех плейтах одной локации.
- Там, где будет превращение, наложи старт и цель 50/50: опорные линии должны совпасть, допуск ~10 px на 1080 px высоты. Если пользователь загрузил картинки и доступно выполнение кода — сделай наложение сам (Python, PIL: `Image.blend(a, b, 0.5)`). Поехало — правка от предыдущего состояния, одним параметром.
- Показать пользователю, получить «ок» — только потом видео.
