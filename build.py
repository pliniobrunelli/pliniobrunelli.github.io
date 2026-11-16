"""Gera o site da Brunelli Games (GitHub Pages). Edite CONFIG e rode: python3 build.py <pasta-de-saida>"""
import sys, pathlib, html

CONFIG = {
    "developer": "Brunelli Games",
    "owner": "Plínio Brunelli",
    "email": "brunelli.games@outlook.com",
    "publisher_id": "pub-8919732037503853",
    "effective_pt": "16 de novembro de 2026",
    "effective_en": "November 16, 2026",
}

GAMES = {
    "cellgenius": {
        "name": "Cell Genius",
        "tag_pt": "Jogo de memória: repita a sequência de casas com a Vó Matilde.",
        "tag_en": "Memory game: repeat the sequence of cells with Granny Matilde.",
        "local_pt": "configurações, recordes (com o nome que você digitar), a partida em andamento e se o tutorial já foi visto",
        "local_en": "settings, high scores (with the name you type), the game in progress and whether the tutorial was seen",
        "reward_pt": "continuar uma partida",
        "reward_en": "continue a game",
    },
    "cellbreaker": {
        "name": "Cell Breaker",
        "tag_pt": "Quebra-cabeça de pares: limpe o tabuleiro com estratégia.",
        "tag_en": "Pair puzzle: clear the board with strategy.",
        "local_pt": "configurações, recordes (com o nome que você digitar), a partida em andamento, o progresso das fases e as ferramentas guardadas",
        "local_en": "settings, high scores (with the name you type), the game in progress, level progress and stored tools",
        "reward_pt": "ganhar ferramentas",
        "reward_en": "earn tools",
    },
}

CSS = """:root{--ink:#2b2550;--muted:#6b6590;--accent:#e08a00;--bg:#fff;--card:#fffaf0;--line:#ece6d6}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 20px 64px}a{color:var(--accent)}
header.site{display:flex;align-items:center;gap:12px;margin-bottom:28px}header.site img{height:44px}
header.site a{text-decoration:none;color:var(--muted);font-weight:600}
h1{font-size:30px;line-height:1.2;margin:0 0 6px}h2{font-size:20px;margin:32px 0 8px}
.muted{color:var(--muted)}.lang{float:right;font-weight:600}
.hero{text-align:center;margin:8px 0 36px}.hero img{width:min(420px,90%)}
.games{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.game{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px;display:flex;gap:14px;align-items:flex-start}
.game img{width:72px;height:72px;border-radius:16px;flex:none}.game h3{margin:0 0 4px}.game p{margin:0 0 8px}
.soon{display:inline-block;background:#fff3d6;color:#8a5a00;border-radius:99px;padding:2px 10px;font-size:13px;font-weight:600}
footer{margin-top:48px;color:var(--muted);font-size:14px;text-align:center}
li{margin:4px 0}"""

def page(title, body, lang, depth):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{up}style.css">
<link rel="icon" href="{up}img/cellgenius.webp">
</head>
<body><main>
<header class="site"><a href="{up}"><img src="{up}img/brunelli-games.webp" alt="{CONFIG['developer']}"></a></header>
{body}
<footer>© 2026 {CONFIG['developer']} · <a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a></footer>
</main></body></html>
"""

def privacy_pt(g):
    c = CONFIG
    return f"""<a class="lang" href="../privacy/">English</a>
<h1>Política de privacidade — {g['name']}</h1>
<p class="muted">Vigente desde {c['effective_pt']}</p>
<p>Esta política explica quais dados o aplicativo <strong>{g['name']}</strong>, da {c['developer']} ({c['owner']}), usa e por quê.</p>

<h2>1. Dados guardados no seu aparelho</h2>
<p>O jogo guarda no próprio aparelho: {g['local_pt']}. Esses dados <strong>não são enviados</strong> a nós nem a terceiros e são apagados se você desinstalar o app ou limpar os dados dele.</p>

<h2>2. Anúncios (Google AdMob)</h2>
<p>O jogo é gratuito e exibe anúncios do Google AdMob (banner, anúncio entre partidas e o anúncio opcional para {g['reward_pt']}). Para mostrar e medir anúncios, o Google pode coletar dados como o identificador de publicidade do aparelho, endereço IP, informações do aparelho e do sistema e interações com os anúncios.</p>
<ul>
<li>No Espaço Econômico Europeu, no Reino Unido e na Suíça, o app pede o seu consentimento antes de mostrar anúncios personalizados. Você pode mudar a escolha em <strong>Configurações → Privacidade</strong>.</li>
<li>Nos estados dos EUA com leis de privacidade (como a Califórnia), você pode recusar a "venda ou compartilhamento" dos seus dados para anúncios em <strong>Configurações → Privacidade</strong>.</li>
<li>Você pode redefinir ou desativar o identificador de publicidade nas configurações do Android.</li>
<li>Como o Google usa esses dados: <a href="https://policies.google.com/technologies/partner-sites">policies.google.com/technologies/partner-sites</a>.</li>
</ul>

<h2>3. Compra "Remover anúncios"</h2>
<p>A compra é feita pelo Google Play. O pagamento e os dados dele ficam com o Google; o app recebe apenas a confirmação de que a compra existe, para tirar os anúncios.</p>

<h2>4. Permissões</h2>
<ul>
<li><strong>Internet e estado da rede</strong>: carregar anúncios e consultar a compra. O jogo funciona sem internet.</li>
<li><strong>Vibração</strong>: resposta tátil no jogo (pode ser desligada nas Configurações).</li>
</ul>

<h2>5. Crianças</h2>
<p>O jogo não é direcionado a crianças menores de 13 anos e não coleta intencionalmente dados pessoais delas.</p>

<h2>6. Seus direitos (LGPD)</h2>
<p>Como não recebemos dados pessoais seus, não há cadastro para consultar ou apagar do nosso lado. Os dados do jogo ficam no seu aparelho e você pode apagá-los a qualquer momento. Para os dados tratados pelo Google, use as ferramentas do Google ou fale conosco.</p>

<h2>7. Alterações e contato</h2>
<p>Se esta política mudar, a nova versão será publicada nesta página com a data atualizada. Dúvidas: <a href="mailto:{c['email']}">{c['email']}</a>.</p>
"""

def privacy_en(g):
    c = CONFIG
    return f"""<a class="lang" href="../privacidade/">Português</a>
<h1>Privacy policy — {g['name']}</h1>
<p class="muted">Effective {c['effective_en']}</p>
<p>This policy explains what data the <strong>{g['name']}</strong> app, by {c['developer']} ({c['owner']}), uses and why.</p>

<h2>1. Data stored on your device</h2>
<p>The game stores on your device: {g['local_en']}. This data is <strong>not sent</strong> to us or to third parties and is deleted if you uninstall the app or clear its data.</p>

<h2>2. Ads (Google AdMob)</h2>
<p>The game is free and shows Google AdMob ads (banner, ads between games and the optional ad to {g['reward_en']}). To show and measure ads, Google may collect data such as the device advertising ID, IP address, device and system information and ad interactions.</p>
<ul>
<li>In the European Economic Area, the United Kingdom and Switzerland, the app asks for your consent before showing personalized ads. You can change your choice in <strong>Settings → Privacy</strong>.</li>
<li>In US states with privacy laws (such as California), you can opt out of the "sale or sharing" of your data for ads in <strong>Settings → Privacy</strong>.</li>
<li>You can reset or turn off the advertising ID in Android settings.</li>
<li>How Google uses this data: <a href="https://policies.google.com/technologies/partner-sites">policies.google.com/technologies/partner-sites</a>.</li>
</ul>

<h2>3. "Remove ads" purchase</h2>
<p>The purchase is made through Google Play. Payment and its data stay with Google; the app only receives confirmation that the purchase exists, to remove the ads.</p>

<h2>4. Permissions</h2>
<ul>
<li><strong>Internet and network state</strong>: loading ads and checking the purchase. The game works offline.</li>
<li><strong>Vibration</strong>: haptic feedback (can be turned off in Settings).</li>
</ul>

<h2>5. Children</h2>
<p>The game is not directed to children under 13 and does not knowingly collect their personal data.</p>

<h2>6. Your rights</h2>
<p>Since we receive no personal data from you, there is no account on our side to access or delete. Game data stays on your device and you can delete it at any time. For data processed by Google, use Google's tools or contact us.</p>

<h2>7. Changes and contact</h2>
<p>If this policy changes, the new version will be published on this page with an updated date. Questions: <a href="mailto:{c['email']}">{c['email']}</a>.</p>
"""

def home():
    cards = ""
    for key, g in GAMES.items():
        cards += f"""<div class="game"><img src="img/{key}.webp" alt="{g['name']}">
<div><h3>{g['name']}</h3><p>{g['tag_pt']}<br><span class="muted">{g['tag_en']}</span></p>
<span class="soon">Em breve no Google Play</span>
<p style="margin-top:8px"><a href="{key}/privacidade/">Política de privacidade</a> · <a href="{key}/privacy/">Privacy policy</a></p></div></div>
"""
    return f"""<div class="hero"><img src="img/brunelli-games.webp" alt="{CONFIG['developer']}"></div>
<p style="text-align:center">Jogos casuais para Android, feitos com carinho.<br><span class="muted">Casual games for Android, made with care.</span></p>
<div class="games">
{cards}</div>
"""

def main(out):
    out = pathlib.Path(out)
    (out / "style.css").write_text(CSS, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    (out / "index.html").write_text(page(CONFIG["developer"], home(), "pt-BR", 0), encoding="utf-8")
    (out / "404.html").write_text(page("404", '<h1>Página não encontrada</h1><p><a href="/">Voltar ao início</a></p>', "pt-BR", 0), encoding="utf-8")
    (out / "app-ads.txt").write_text(f"google.com, {CONFIG['publisher_id']}, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")
    for key, g in GAMES.items():
        for folder, fn, lang in (("privacidade", privacy_pt, "pt-BR"), ("privacy", privacy_en, "en")):
            d = out / key / folder
            d.mkdir(parents=True, exist_ok=True)
            title = ("Política de privacidade" if lang == "pt-BR" else "Privacy policy") + f" — {g['name']}"
            (d / "index.html").write_text(page(title, fn(g), lang, 2), encoding="utf-8")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
