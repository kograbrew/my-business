# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

KOGRA is a kombucha producer focused on B2B wholesale (also sells retail to anyone) (bars, cafes, saunas, gyms, shops; Kyiv, Kharkiv, Berestyn, Uman). This repo holds the business brief, the website copy, and a one-page static site. There is no build system, package manager, linter or test suite. All content is in **Ukrainian**; keep new copy, comments and commit messages in Ukrainian.

## Files and how they relate

- [brief.md](brief.md) — source of truth for facts: products, flavours, composition, prices (60 UAH/bottle, minimum 24 pcs = 1 440 UAH), delivery rules, shelf life, tasting-set terms, response hours. Check it before writing any number or claim.
- [site-texts.md](site-texts.md) — full copy for the planned multi-block one-page site, in page order. `[уточнити]` marks items that must be confirmed before launch.
- [index.html](index.html) — the currently built page: a single self-contained file (inline CSS, no JS, no dependencies) with light/dark theming via CSS variables and `prefers-color-scheme`. It implements only a short subset of site-texts.md (hero, three benefit bullets, CTA to Instagram `kogra.brew`). Open it directly in a browser to preview.
- [slogans.py](slogans.py) — stdlib-only script that sends brief.md to a free OpenRouter model and prints raw JSON plus the reply.

Facts in index.html and site-texts.md must stay consistent with brief.md (the site focuses on B2B, but retail exists: 95 UAH/bottle for anyone; min 6 bottles, retail ships via Nova Poshta).

## Running the slogan script

```
python3 slogans.py                 # tries up to 10 free (":free") models in turn until one answers
python3 slogans.py <model-id>      # use one specific model
```

It reads `OPENROUTER_API_KEY` from a local `.env` (git-ignored; never commit or print it). The prompt tells the model not to invent prices.

## Бізнес

**Хто ми**
- KOGRA — виробництво й оптовий продаж комбучі для бізнесу, а також роздріб. Київ і Харків — основні міста, ще Берестин і Умань; по Україні доставляємо Новою Поштою.
- Головна пропозиція: м'яка комбуча (легкий газ, свіжість, гарна пляшка), яку заклад може безкоштовно спробувати до закупівлі.

**Для кого сайт і головна дія**
- Фокус сайту — B2B: бари, кафе, фастфуд, бані й сауни, спортклуби, магазини. Роздріб теж є: купити може будь-хто, 95 грн/пляшка, мінімум 6 пляшок (наприклад, по 2 кожного смаку; смаки можна комбінувати), доставка роздрібу — Новою Поштою. Замовити можна в Instagram, Telegram або на пошту kograinfo@gmail.com.
- Головна дія — кнопка «Замовити дегустаційний набір» (форма: ім'я, заклад, тип, місто, телефон; заявка йде в Telegram). Друга дія — «Зробити оптове замовлення».

**Тон текстів**
- Українською, на «ви», дружньо, але по-діловому; просто й тепло, без канцеляриту й пафосу.
- Короткі речення, конкретика: цифри, умови, вигода для закладу.

**Послуги й ціни (тільки з brief.md)**
- Комбуча 0,33 л, три смаки: Класика, Жасмин (хіт), Каркаде. Опт 60 грн/пляшка, мінімум 24 шт (1 440 грн); роздріб 95 грн/пляшка, мінімум 6 шт, смаки можна поєднувати.
- Дегустаційний набір: 3 пляшки (по одній кожного смаку), безкоштовно, один на заклад. У Києві привозимо самі, в інші міста доставку НП оплачує отримувач.
- Доставка: Київ від 24 шт — своїм транспортом, безкоштовно; інші міста — Новою Поштою.
- Бонус за перше замовлення протягом 14 днів після дегустації: +1 пляшка на кожні 12 (запасний варіант — знижка 5%).
- Зберігання: 90 днів, у холодильнику +2…+6 °C. Відповідь на заявку: 10:00–19:00 протягом 10 хвилин.

**Заборони**
- Не вигадувати ціни, знижки, адреси й відгуки. Якщо чогось немає в brief.md — спитати мене.
- Ключі з .env ніколи не виводити в чат чи лог і не вписувати в код.
- Без моєї згоди нічого не відправляти на GitHub (push, PR, issues).
