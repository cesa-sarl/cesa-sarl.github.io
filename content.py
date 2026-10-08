"""Content data for the CESA site. Consumed by build.py."""

SITE_URL = "https://cesa-sarl.github.io/"


def IMG(cat, name):
    return f"assets/img/{cat}/{name}"

SITE = {
    "name": "CESA",
    "phone_display": "+229 21 32 57 87",
    "phone_tel": "+22921325787",
    "phone2_display": "+229 95 98 21 70",
    "phone2_tel": "+22995982170",
    "phone3_display": "+229 97 12 62 76",
    "phone3_tel": "+22997126276",
    "email": "cesa@rtb.bj",
    "whatsapp": "22997126276",
    "rccm": "R.C.C.M. B/N° 97 K / 2000-B/00191, Cotonou",
    "address_line1": "C/22 Bis Gbèdjèwin, ruelle en face de la Quincaillerie « La Tour », non loin du carrefour de l'Église Sacré-Cœur",
    "address_line2": "Akpakpa, Cotonou, République du Bénin",
    "maps_embed_src": "https://www.google.com/maps?q=Entreprise+CESA+Sarl,6.3713825,2.4482162&z=16&output=embed",
    "maps_link": "https://www.google.com/maps/place/Entreprise+CESA+Sarl/@6.3713825,2.4482162,17z/data=!3m1!4b1!4m6!3m5!1s0x102355fba76cbec9:0xc82c812a9142dbbd!8m2!3d6.3713825!4d2.4482162!16s%2Fg%2F11rg8vppk9",
}

NAV = {
    "expertises": [
        ("Énergie Solaire", "energie-solaire.html"),
        ("Électricité", "electricite.html"),
        ("Climatisation", "climatisation.html"),
        ("Sanitaire", "sanitaire.html"),
        ("Acoustique", "acoustique.html"),
        ("Sécurité & Protection Incendie", "securite-protection.html"),
        ("Ascenseurs", "ascenseurs.html"),
        ("Communication & Réseaux", "communication-reseaux.html"),
        ("Génie Civil & Génie-Conseil", "genie-civil.html"),
    ],
    # Shorter labels for the footer's two-column link grid.
    "expertises_short": [
        ("Énergie Solaire", "energie-solaire.html"),
        ("Électricité", "electricite.html"),
        ("Climatisation", "climatisation.html"),
        ("Sanitaire", "sanitaire.html"),
        ("Acoustique", "acoustique.html"),
        ("Sécurité Incendie", "securite-protection.html"),
        ("Ascenseurs", "ascenseurs.html"),
        ("Communication", "communication-reseaux.html"),
        ("Génie Civil", "genie-civil.html"),
    ],
}

CLIENT_LOGOS = [
    {"file": "asecna.jpg", "name": "ASECNA"},
    {"file": "bgfi.jpg", "name": "BGFI Bénin"},
    {"file": "franzetti.jpg", "name": "Franzetti Bénin"},
    {"file": "gouvernement-benin.jpg", "name": "Gouvernement du Bénin"},
    {"file": "boa.jpg", "name": "BOA Bénin"},
    {"file": "ecobank.jpg", "name": "Ecobank"},
    {"file": "cdpa.jpg", "name": "CDPA"},
    {"file": "diamond-bank.jpg", "name": "Diamond Bank"},
    {"file": "plan-international.jpg", "name": "Plan International"},
    {"file": "agrisatch.jpg", "name": "Agrisatch"},
    {"file": "banque-atlantique.jpg", "name": "Banque Atlantique"},
    {"file": "bsic.jpg", "name": "BSIC"},
    {"file": "insae.jpg", "name": "INSAE"},
    {"file": "uba.jpg", "name": "UBA Bénin"},
    {"file": "unicef.jpg", "name": "UNICEF"},
    {"file": "edil-group-btp.jpg", "name": "Edil Group BTP"},
    {"file": "agetur.jpg", "name": "AGETUR"},
    {"file": "port-autonome-cotonou.jpg", "name": "Port Autonome de Cotonou"},
]

CLIENTS_MORE = "+ de nombreux clients institutionnels et privés au Bénin, dans la banque, l'industrie et les organisations internationales."

SECTORS = [
    {"icon": "building", "title": "Banque & Finance", "text": "BGFI, BOA, Ecobank, UBA, Diamond Bank, Banque Atlantique, BSIC."},
    {"icon": "shield", "title": "Institutions publiques", "text": "Gouvernement du Bénin, INSAE, AGETUR, Présidence de la République."},
    {"icon": "globe", "title": "Organisations internationales", "text": "ASECNA, UNICEF, Plan International."},
    {"icon": "crane", "title": "Industrie & BTP", "text": "Franzetti, Edil Group BTP, CDPA, Agrisatch, Port Autonome de Cotonou."},
]

BUILDING_PHOTO = IMG("brand", "batiment-cesa.jpg")

# ---------------------------------------------------------------------------
# PAGES
# ---------------------------------------------------------------------------
PAGES = []

def add(page):
    PAGES.append(page)

# ============================================================ HOME =========
add({
    "slug": "index.html",
    "template": "home",
    "title": "Énergie Solaire, Électricité & Climatisation au Bénin",
    "description": "CESA, firme d'ingénierie basée à Cotonou : énergie solaire, électricité, climatisation, sanitaire, acoustique, protection incendie, ascenseurs et génie civil. 25 ans d'expérience au Bénin.",
    "nav_active": "home",
    "hero": {
        "slides": [BUILDING_PHOTO, IMG("hero", "home-2.svg"), IMG("hero", "home-3.svg")],
        "eyebrow": "Firme d'ingénierie · 25 ans d'expérience à Cotonou",
        "title": "Votre partenaire de confiance en <span>énergie</span> et en <span>électricité</span>",
        "lead": "CESA conçoit, installe et entretient les équipements d'énergie, d'électricité, de climatisation et de sécurité qui font fonctionner les bâtiments publics et privés du Bénin, de l'aéroport de Cadjehoun à la Présidence de la République.",
        "cta": {"label": "Découvrir nos expertises", "href": "expertises.html"},
        "cta2": {"label": "Qui sommes-nous", "href": "a-propos.html"},
        "stats": [
            {"num": "25 ans", "label": "D'expérience de terrain"},
            {"num": "9", "label": "Domaines d'expertise complémentaires"},
            {"num": "18+", "label": "Références institutionnelles & bancaires"},
            {"num": "100%", "label": "Interventions et SAV à Cotonou"},
        ],
    },
    "pillars": [
        {"icon": "bolt", "title": "Énergie & Électricité", "text": "Solaire, électricité bâtiment & réseau MT, groupes électrogènes, éclairage public.", "href": "expertises.html"},
        {"icon": "snow", "title": "Confort & Habitat", "text": "Climatisation, sanitaire et acoustique, pour un cadre de vie et de travail maîtrisé.", "href": "expertises.html"},
        {"icon": "shield", "title": "Sécurité, Bâtiment & Réseaux", "text": "Ascenseurs, protection incendie, communication et génie civil.", "href": "expertises.html"},
    ],
    "sections": [
        {
            "type": "split", "id": "qui-sommes-nous",
            "eyebrow": "Qui sommes-nous",
            "title": "CESA, le partenaire <span>de confiance</span> pour vos projets d'ingénierie",
            "lead": "CESA est une entreprise d'énergie et d'ingénierie basée à Cotonou, au Bénin, en Afrique de l'Ouest.",
            "paragraphs": [
                "Avec 25 ans d'expérience, CESA fournit des services spécialisés en climatisation, électricité, énergie solaire, sanitaire et acoustique, ainsi qu'en ascenseurs, groupes électrogènes, protection incendie, protection contre les surtensions atmosphériques, communication et génie civil.",
                "Que ce soit à l'Aéroport International de Cadjehoun, à la Présidence de la République ou lors de l'éclairage de divers axes routiers de Cotonou, nos équipes conçoivent et exécutent des solutions adaptées aux besoins de nos clients, publics comme privés.",
            ],
            "bullets": [
                "25 ans d'expérience, partenaires européens, américains et chinois",
                "Études, expertises, plans, réalisations et entretiens",
                "Installation, maintenance et service après-vente assurés localement à Cotonou",
            ],
            "cta": {"label": "Qui sommes-nous", "href": "a-propos.html"},
            "image": BUILDING_PHOTO,
            "badge": {"icon": "award", "text": "25 ans d'expérience"},
        },
        {
            "type": "category-grid", "bg": "alt", "id": "metiers",
            "eyebrow": "Nos expertises", "cols": 3,
            "title": "Neuf domaines, <span>une seule</span> exigence d'excellence",
            "lead": "De la production d'énergie au confort du bâtiment, CESA couvre l'ensemble des métiers techniques de vos infrastructures, appuyé par une activité transversale de génie-conseil.",
            "cards": [
                {"image": IMG("realisations", "upp-solaire-1mw-2018.jpg"), "tag": "Énergie", "title": "Énergie Solaire", "text": "Centrales et kits photovoltaïques, étude et dimensionnement.", "href": "energie-solaire.html"},
                {"image": IMG("expertises", "electricite-collage.jpg"), "tag": "Électricité", "title": "Électricité", "text": "Bâtiment, réseau MT, groupes électrogènes, éclairage public.", "href": "electricite.html"},
                {"image": IMG("expertises", "climatisation-collage.jpg"), "tag": "Confort", "title": "Climatisation", "text": "Résidentiel, tertiaire et industriel, étude et maintenance.", "href": "climatisation.html"},
                {"image": IMG("expertises", "sanitaire-photo.jpg"), "tag": "Sanitaire", "title": "Sanitaire", "text": "Plomberie, distribution d'eau et évacuations.", "href": "sanitaire.html"},
                {"image": IMG("expertises", "acoustique-photo.jpg"), "tag": "Acoustique", "title": "Acoustique", "text": "Isolation et correction acoustique des locaux.", "href": "acoustique.html"},
                {"image": IMG("expertises", "securite-photo.jpg"), "tag": "Sécurité", "title": "Sécurité & Protection Incendie", "text": "Protection incendie eau & détection, protection contre les surtensions.", "href": "securite-protection.html"},
                {"image": IMG("expertises", "ascenseurs-photo.jpg"), "tag": "Levage", "title": "Ascenseurs", "text": "Installation, modernisation et maintenance d'ascenseurs.", "href": "ascenseurs.html"},
                {"image": IMG("expertises", "communication-photo.jpg"), "tag": "Réseaux", "title": "Communication & Réseaux", "text": "Réseaux informatiques, télécommunications, vidéosurveillance.", "href": "communication-reseaux.html"},
                {"image": IMG("expertises", "genie-civil-photo.jpg"), "tag": "Bâtiment", "title": "Génie Civil & Génie-Conseil", "text": "Études techniques, travaux de génie civil, supervision de chantiers.", "href": "genie-civil.html"},
            ],
        },
        {
            "type": "gallery", "id": "apercu-realisations",
            "eyebrow": "Nos réalisations",
            "title": "Un aperçu de <span>nos chantiers</span>",
            "lead": "Aéroport de Cotonou, siège de CDPA, centrale solaire industrielle : quelques repères parmi nos interventions.",
            "images": [
                {"src": IMG("realisations", "aeroport-arrivee-2012.jpg"), "alt": "Extension du hall Arrivée, Aéroport Cardinal Bernardin Gantin"},
                {"src": IMG("realisations", "upp-solaire-1mw-2018.jpg"), "alt": "Centrale solaire de 1 MW, Usine UPP"},
                {"src": IMG("realisations", "cdpa-siege-2013.jpg"), "alt": "Siège de CDPA"},
                {"src": IMG("realisations", "eclairage-solaire-routier.jpg"), "alt": "Éclairage solaire d'un axe routier"},
            ],
            "big_indexes": [0],
        },
        {
            "type": "clients", "bg": "alt", "id": "clients",
            "eyebrow": "Ils nous font confiance",
            "title": "Nos <span>partenaires</span> et clients",
            "logos": CLIENT_LOGOS,
            "more": CLIENTS_MORE,
        },
        {
            "type": "cta-banner",
            "title": "Un projet d'ingénierie à nous confier ?",
            "text": "Énergie, électricité, climatisation, sécurité : parlons de vos besoins et de vos délais.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
            "secondary": {"label": "Voir nos réalisations", "href": "realisations.html"},
        },
    ],
})

# ============================================================ À PROPOS =====
add({
    "slug": "a-propos.html",
    "template": "inner",
    "title": "Qui sommes-nous",
    "description": "CESA est une firme d'ingénierie basée à Cotonou, au Bénin, avec 25 ans d'expérience en énergie, électricité, climatisation et génie civil.",
    "nav_active": "a-propos",
    "hero": {
        "image": BUILDING_PHOTO,
        "breadcrumb": [("Accueil", "index.html"), ("À propos", "a-propos.html")],
        "eyebrow": "Qui sommes-nous",
        "title": "25 ans d'expérience <span>au service</span> de vos projets",
        "lead": "CESA est une entreprise d'énergie et d'ingénierie basée à Cotonou, au Bénin, en Afrique de l'Ouest.",
    },
    "sections": [
        {
            "type": "split", "id": "histoire",
            "eyebrow": "Notre histoire",
            "title": "Une firme d'ingénierie <span>pluridisciplinaire</span>",
            "paragraphs": [
                "Depuis 25 ans, CESA accompagne ses clients publics et privés dans la conception, l'installation et la maintenance de leurs équipements techniques : climatisation, électricité, énergie solaire, sanitaire, acoustique, ascenseurs, groupes électrogènes, protection incendie, protection contre les surtensions atmosphériques, communication et génie civil.",
                "Nous travaillons avec des partenaires européens, américains et chinois afin de fournir à notre clientèle des équipements de pointe. Nos voyages en usines et nos liens étroits avec ces partenaires nous permettent d'être à l'affût des dernières technologies et de les adapter efficacement à un pays tropical comme le Bénin.",
                "Au-delà de l'installation, CESA est sollicitée pour des prestations de génie-conseil et de consultation sur des projets publics et privés, en appui aux maîtres d'ouvrage et maîtres d'œuvre : études, expertises, plans, réalisations et entretiens.",
            ],
            "bullets": [
                "Aéroport International de Cadjehoun, Présidence de la République, éclairage de divers axes routiers",
                "Partenariats industriels en Europe, aux États-Unis et en Chine",
                "Génie-conseil et consultation sur des projets d'envergure",
            ],
            "cta": {"label": "Nos expertises", "href": "expertises.html"},
            "image": IMG("expertises", "genie-civil-photo.jpg"),
            "badge": {"icon": "award", "text": "25 ans d'expérience"},
        },
        {
            "type": "feature-grid", "bg": "alt", "id": "valeurs",
            "eyebrow": "Nos valeurs", "cols": 4,
            "title": "Ce qui guide <span>notre travail</span>",
            "lead": "Une exigence technique constante, au service de la durabilité de vos installations.",
            "cards": [
                {"icon": "tool", "title": "Exigence technique", "text": "Des équipes formées en continu et des équipements certifiés auprès de nos partenaires."},
                {"icon": "globe", "title": "Veille technologique", "text": "Des liens étroits avec des fabricants européens, américains et chinois."},
                {"icon": "headset", "title": "Proximité & SAV", "text": "Une présence et un service après-vente assurés localement à Cotonou."},
                {"icon": "graduate", "title": "Génie-conseil", "text": "Études techniques et consultation en appui de vos décisions de projet."},
            ],
        },
        {
            "type": "timeline", "id": "demarche",
            "eyebrow": "Notre démarche",
            "title": "De l'étude <span>à la maintenance</span>",
            "lead": "Une méthode éprouvée sur chaque projet, quel que soit le domaine technique concerné.",
            "cards": [
                {"title": "Étude & conseil", "text": "Analyse du besoin, dimensionnement technique et recommandations de génie-conseil."},
                {"title": "Conception", "text": "Choix des équipements et des partenaires adaptés au projet et au climat local."},
                {"title": "Réalisation", "text": "Installation par nos équipes techniques, dans le respect des délais et des normes."},
                {"title": "Maintenance & SAV", "text": "Contrats d'entretien et interventions pour garantir la durabilité des installations."},
            ],
        },
        {
            "type": "cta-banner",
            "title": "Envie d'en savoir plus sur nos expertises ?",
            "text": "Découvrez nos neuf domaines d'intervention, du solaire au génie civil.",
            "primary": {"label": "Nos expertises", "href": "expertises.html"},
            "secondary": {"label": "Nous contacter", "href": "contact.html"},
        },
    ],
})

# ============================================================ EXPERTISES ===
add({
    "slug": "expertises.html",
    "template": "inner",
    "title": "Nos Expertises",
    "description": "Climatisation, électricité, énergie solaire, sanitaire, acoustique, ascenseurs, protection incendie, communication et génie civil : les neuf domaines d'expertise de CESA.",
    "nav_active": "expertises",
    "hero": {
        "image": IMG("hero", "expertises.svg"),
        "breadcrumb": [("Accueil", "index.html"), ("Nos expertises", "expertises.html")],
        "eyebrow": "Nos expertises",
        "title": "Neuf domaines, <span>une seule</span> exigence d'excellence",
        "lead": "CESA couvre l'ensemble des métiers techniques qui font fonctionner un bâtiment ou une infrastructure, avec en transversal une activité de génie-conseil sur chacun de ces domaines.",
    },
    "sections": [
        {
            "type": "category-grid", "cols": 3,
            "eyebrow": "Vue d'ensemble",
            "title": "Découvrez <span>nos neuf</span> domaines de services",
            "cards": [
                {"image": IMG("realisations", "upp-solaire-1mw-2018.jpg"), "tag": "Énergie", "title": "Énergie Solaire", "text": "Centrales et kits photovoltaïques, étude et dimensionnement.", "href": "energie-solaire.html"},
                {"image": IMG("expertises", "electricite-collage.jpg"), "tag": "Électricité", "title": "Électricité", "text": "Bâtiment, réseau moyenne tension, groupes électrogènes, éclairage public.", "href": "electricite.html"},
                {"image": IMG("expertises", "climatisation-collage.jpg"), "tag": "Confort", "title": "Climatisation", "text": "Résidentiel, tertiaire, industriel : étude, installation et maintenance.", "href": "climatisation.html"},
                {"image": IMG("expertises", "sanitaire-photo.jpg"), "tag": "Sanitaire", "title": "Sanitaire", "text": "Plomberie, distribution d'eau, évacuations et équipements sanitaires.", "href": "sanitaire.html"},
                {"image": IMG("expertises", "acoustique-photo.jpg"), "tag": "Acoustique", "title": "Acoustique", "text": "Isolation phonique et correction acoustique des locaux.", "href": "acoustique.html"},
                {"image": IMG("expertises", "securite-photo.jpg"), "tag": "Sécurité", "title": "Sécurité & Protection Incendie", "text": "Protection incendie eau & détection, protection contre les surtensions atmosphériques.", "href": "securite-protection.html"},
                {"image": IMG("expertises", "ascenseurs-photo.jpg"), "tag": "Levage", "title": "Ascenseurs", "text": "Installation, modernisation, maintenance préventive et corrective.", "href": "ascenseurs.html"},
                {"image": IMG("expertises", "communication-photo.jpg"), "tag": "Réseaux", "title": "Communication & Réseaux", "text": "Réseaux informatiques, télécommunications, vidéosurveillance.", "href": "communication-reseaux.html"},
                {"image": IMG("expertises", "genie-civil-photo.jpg"), "tag": "Bâtiment", "title": "Génie Civil & Génie-Conseil", "text": "Études techniques, travaux de génie civil, supervision de chantiers.", "href": "genie-civil.html"},
            ],
        },
        {
            "type": "cta-banner",
            "title": "Un besoin qui touche plusieurs de ces domaines ?",
            "text": "Nos équipes coordonnent les interventions multi-métiers sur un même site.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
            "secondary": {"label": "Qui sommes-nous", "href": "a-propos.html"},
        },
    ],
})


def expertise_page(slug, title, description, eyebrow, hero_title, hero_lead, intro_paragraphs, intro_bullets, badge_text, image, feature_cards):
    add({
        "slug": slug,
        "template": "inner",
        "title": title,
        "description": description,
        "nav_active": "expertises",
        "hero": {
            "image": image,
            "breadcrumb": [("Accueil", "index.html"), ("Nos expertises", "expertises.html"), (title, slug)],
            "eyebrow": eyebrow,
            "title": hero_title,
            "lead": hero_lead,
        },
        "sections": [
            {
                "type": "split", "id": "presentation",
                "paragraphs": intro_paragraphs,
                "bullets": intro_bullets,
                "cta": {"label": "Demander un devis", "href": "contact.html"},
                "image": image,
                "badge": {"icon": "check", "text": badge_text},
            },
            {
                "type": "feature-grid", "bg": "alt", "cols": len(feature_cards),
                "eyebrow": "Nos prestations",
                "title": "Ce que nous proposons",
                "cards": feature_cards,
            },
            {
                "type": "cta-banner",
                "title": "Un projet dans ce domaine ?",
                "text": "Décrivez-nous votre besoin, nous revenons vers vous rapidement.",
                "primary": {"label": "Nous contacter", "href": "contact.html"},
                "secondary": {"label": "Toutes nos expertises", "href": "expertises.html"},
            },
        ],
    })


expertise_page(
    slug="energie-solaire.html",
    title="Énergie Solaire",
    description="Centrales et kits solaires photovoltaïques : étude, dimensionnement et installation par CESA au Bénin.",
    eyebrow="Énergie",
    hero_title="Énergie <span>Solaire</span>",
    hero_lead="Des solutions photovoltaïques étudiées et dimensionnées pour le climat et les besoins du Bénin.",
    intro_paragraphs=[
        "CESA fournit des services spécialisés en énergie solaire : étude, dimensionnement et installation de centrales et kits photovoltaïques pour sites résidentiels, tertiaires, industriels ou isolés.",
        "Associée à nos expertises en électricité, l'énergie solaire permet de sécuriser l'alimentation de sites sensibles ou éloignés du réseau, avec un entretien assuré localement à Cotonou.",
    ],
    intro_bullets=[
        "Centrales et kits solaires photovoltaïques",
        "Étude et dimensionnement selon le site et les besoins",
        "Solutions autonomes pour sites isolés du réseau",
        "Maintenance et suivi de performance",
    ],
    badge_text="Partenaires européens, américains & chinois",
    image=IMG("realisations", "upp-solaire-1mw-2018.jpg"),
    feature_cards=[
        {"icon": "sun", "title": "Centrales solaires", "text": "Études, dimensionnement et installation de centrales photovoltaïques."},
        {"icon": "gear", "title": "Kits solaires", "text": "Solutions clé en main pour sites isolés ou en appoint réseau."},
        {"icon": "tool", "title": "Maintenance", "text": "Suivi de performance et entretien des installations."},
    ],
)

expertise_page(
    slug="electricite.html",
    title="Électricité",
    description="Électricité de bâtiment et de réseau moyenne tension, groupes électrogènes, éclairage public : les services électricité de CESA au Bénin.",
    eyebrow="Électricité",
    hero_title="<span>Électricité</span> Bâtiment & Réseau",
    hero_lead="Câblage, tableaux, postes moyenne tension et groupes électrogènes : l'électricité maîtrisée, du bâtiment à l'infrastructure publique.",
    intro_paragraphs=[
        "CESA conçoit et installe des infrastructures électriques de bâtiment et de réseau moyenne tension, ainsi que l'éclairage public, à l'image de l'éclairage de divers axes routiers de Cotonou.",
        "Nous fournissons et installons également des groupes électrogènes de toute puissance, pour sécuriser l'alimentation électrique des sites sensibles : hôpitaux, banques, hôtels, bâtiments administratifs.",
    ],
    intro_bullets=[
        "Électricité bâtiment : câblage, tableaux électriques",
        "Postes et réseaux moyenne tension (MT)",
        "Groupes électrogènes de toute puissance : vente, installation, maintenance",
        "Éclairage public d'axes routiers et d'espaces publics",
    ],
    badge_text="Partenaires européens, américains & chinois",
    image=IMG("expertises", "electricite-collage.jpg"),
    feature_cards=[
        {"icon": "bolt", "title": "Électricité bâtiment & MT", "text": "Câblage, tableaux électriques, postes et réseaux moyenne tension."},
        {"icon": "gear", "title": "Groupes électrogènes", "text": "Vente, installation et maintenance de groupes de toute puissance."},
        {"icon": "building", "title": "Éclairage public", "text": "Éclairage d'axes routiers, de parkings et d'espaces publics."},
    ],
)

expertise_page(
    slug="climatisation.html",
    title="Climatisation",
    description="Climatisation résidentielle, tertiaire et industrielle : étude, installation et maintenance par CESA à Cotonou.",
    eyebrow="Confort",
    hero_title="<span>Climatisation</span>",
    hero_lead="Des solutions de climatisation étudiées pour le climat tropical du Bénin, de l'habitat à l'industrie.",
    intro_paragraphs=[
        "CESA installe et entretient des systèmes de climatisation adaptés à chaque usage : logements, bureaux, hôtels, salles techniques et sites industriels. Nos équipes dimensionnent les installations selon les contraintes propres au climat tropical, pour garantir performance et durabilité.",
        "Un entretien régulier conditionne la performance et la durée de vie des équipements : CESA propose des contrats de maintenance adaptés à chaque site.",
    ],
    intro_bullets=[
        "Climatisation résidentielle et tertiaire (split, multi-split, gainables)",
        "Climatisation industrielle et de salles techniques",
        "Étude thermique et dimensionnement des installations",
        "Contrats de maintenance préventive et corrective",
    ],
    badge_text="Adapté au climat tropical",
    image=IMG("expertises", "climatisation-collage.jpg"),
    feature_cards=[
        {"icon": "snow", "title": "Résidentiel & tertiaire", "text": "Installation de systèmes split, multi-split et gainables."},
        {"icon": "gear", "title": "Industriel", "text": "Climatisation de process et de salles techniques sensibles."},
        {"icon": "tool", "title": "Maintenance", "text": "Contrats d'entretien préventif et interventions correctives."},
    ],
)

expertise_page(
    slug="sanitaire.html",
    title="Sanitaire",
    description="Plomberie, distribution d'eau, évacuations et équipements sanitaires : les services sanitaire de CESA au Bénin.",
    eyebrow="Sanitaire",
    hero_title="<span>Sanitaire</span>",
    hero_lead="Des réseaux d'eau et d'évacuation fiables, conçus pour durer.",
    intro_paragraphs=[
        "CESA conçoit et installe les réseaux sanitaires des bâtiments résidentiels, tertiaires et industriels : distribution d'eau, évacuations, équipements sanitaires.",
        "Ces installations sont pensées en cohérence avec nos autres interventions techniques (électricité, climatisation) pour des bâtiments fonctionnels de bout en bout.",
    ],
    intro_bullets=[
        "Distribution d'eau potable",
        "Réseaux d'évacuation des eaux usées et pluviales",
        "Installation d'équipements sanitaires",
        "Maintenance et dépannage",
    ],
    badge_text="Études, expertises, plans, réalisations",
    image=IMG("expertises", "sanitaire-photo.jpg"),
    feature_cards=[
        {"icon": "drop", "title": "Distribution d'eau", "text": "Réseaux d'alimentation en eau potable."},
        {"icon": "tool", "title": "Évacuations", "text": "Réseaux d'évacuation des eaux usées et pluviales."},
        {"icon": "gear", "title": "Équipements", "text": "Fourniture et installation d'équipements sanitaires."},
    ],
)

expertise_page(
    slug="acoustique.html",
    title="Acoustique",
    description="Isolation phonique et correction acoustique des locaux : les services acoustique de CESA au Bénin.",
    eyebrow="Acoustique",
    hero_title="<span>Acoustique</span>",
    hero_lead="Un confort sonore étudié pour vos espaces de vie et de travail.",
    intro_paragraphs=[
        "CESA propose des solutions d'isolation et de correction acoustique pour les bâtiments résidentiels, tertiaires et institutionnels : salles de réunion, auditoriums, bureaux, chambres d'hôtel.",
        "Chaque projet fait l'objet d'une étude adaptée à l'usage du local et aux contraintes du bâtiment.",
    ],
    intro_bullets=[
        "Isolation phonique entre locaux",
        "Correction acoustique de salles (réunion, auditorium)",
        "Études acoustiques sur mesure",
        "Matériaux et solutions adaptés au climat tropical",
    ],
    badge_text="Études, expertises, plans, réalisations",
    image=IMG("expertises", "acoustique-photo.jpg"),
    feature_cards=[
        {"icon": "wave", "title": "Isolation phonique", "text": "Traitement des parois entre locaux sensibles."},
        {"icon": "graduate", "title": "Étude acoustique", "text": "Diagnostic et recommandations adaptées à l'usage du local."},
        {"icon": "tool", "title": "Correction de salle", "text": "Traitement acoustique de salles de réunion et auditoriums."},
    ],
)

expertise_page(
    slug="securite-protection.html",
    title="Sécurité & Protection Incendie",
    description="Protection incendie eau et détection électronique, protection contre les surtensions atmosphériques : les services sécurité de CESA.",
    eyebrow="Sécurité",
    hero_title="Sécurité & <span>Protection Incendie</span>",
    hero_lead="Protéger les personnes et les biens : réseaux incendie, détection électronique et protection contre la foudre.",
    intro_paragraphs=[
        "CESA conçoit et installe des systèmes de protection incendie eau (poteaux d'incendie, robinets d'incendie armés RIA, réseaux sprinklers), ainsi que des systèmes de détection incendie électronique et d'alarme.",
        "Nous installons également des dispositifs de protection contre les surtensions atmosphériques (parafoudre), indispensables sous les climats à forte activité orageuse comme celui du Bénin.",
    ],
    intro_bullets=[
        "Protection incendie eau : poteaux d'incendie, RIA, sprinklers",
        "Détection incendie électronique et alarme",
        "Protection contre les surtensions atmosphériques (parafoudre)",
        "Audit et mise en conformité sécurité incendie",
    ],
    badge_text="Normes de sécurité incendie",
    image=IMG("expertises", "securite-photo.jpg"),
    feature_cards=[
        {"icon": "drop", "title": "Incendie eau", "text": "Poteaux d'incendie, RIA et réseaux sprinklers."},
        {"icon": "flame", "title": "Détection & alarme", "text": "Systèmes de détection incendie électronique."},
        {"icon": "shield", "title": "Protection surtensions", "text": "Parafoudre et protection contre la foudre."},
    ],
)

expertise_page(
    slug="ascenseurs.html",
    title="Ascenseurs",
    description="Installation, modernisation et maintenance d'ascenseurs par CESA à Cotonou, Bénin.",
    eyebrow="Levage",
    hero_title="Ascenseurs & <span>Équipements de Levage</span>",
    hero_lead="Installation, modernisation et maintenance d'ascenseurs pour bâtiments résidentiels, tertiaires et hôteliers.",
    intro_paragraphs=[
        "CESA installe des ascenseurs neufs et assure la modernisation d'installations existantes, en s'appuyant sur des partenaires industriels européens, américains et chinois.",
        "Parce qu'un ascenseur à l'arrêt immobilise tout un bâtiment, CESA propose des contrats de maintenance préventive et corrective avec intervention rapide à Cotonou.",
    ],
    intro_bullets=[
        "Installation d'ascenseurs neufs (résidentiel, tertiaire, hôtelier)",
        "Modernisation et mise aux normes d'ascenseurs existants",
        "Maintenance préventive et corrective",
        "Contrats de service avec intervention locale",
    ],
    badge_text="Intervention locale à Cotonou",
    image=IMG("expertises", "ascenseurs-photo.jpg"),
    feature_cards=[
        {"icon": "elevator", "title": "Installation", "text": "Ascenseurs neufs pour bâtiments résidentiels et tertiaires."},
        {"icon": "gear", "title": "Modernisation", "text": "Mise aux normes et remplacement de composants."},
        {"icon": "headset", "title": "Maintenance & SAV", "text": "Contrats d'entretien et interventions rapides."},
    ],
)

expertise_page(
    slug="communication-reseaux.html",
    title="Communication & Réseaux",
    description="Réseaux informatiques, télécommunications et vidéosurveillance : les services communication de CESA.",
    eyebrow="Réseaux",
    hero_title="Communication & <span>Réseaux</span>",
    hero_lead="Des infrastructures de communication fiables pour accompagner vos équipements techniques.",
    intro_paragraphs=[
        "CESA conçoit et installe des réseaux informatiques structurés et des solutions de télécommunication d'entreprise, en complément de ses interventions en électricité et en sécurité.",
        "Nos équipes intègrent également des systèmes de vidéosurveillance et de contrôle d'accès, pour sécuriser vos sites professionnels et institutionnels.",
    ],
    intro_bullets=[
        "Réseaux informatiques structurés (câblage, baies de brassage)",
        "Télécommunications d'entreprise",
        "Vidéosurveillance et contrôle d'accès",
        "Intégration avec vos systèmes électriques et de sécurité existants",
    ],
    badge_text="Intégration multi-systèmes",
    image=IMG("expertises", "communication-photo.jpg"),
    feature_cards=[
        {"icon": "network", "title": "Réseaux informatiques", "text": "Câblage structuré et infrastructures réseau d'entreprise."},
        {"icon": "shield", "title": "Vidéosurveillance", "text": "Systèmes de contrôle d'accès et de vidéosurveillance."},
        {"icon": "tool", "title": "Intégration", "text": "Coordination avec vos installations électriques et de sécurité."},
    ],
)

expertise_page(
    slug="genie-civil.html",
    title="Génie Civil & Génie-Conseil",
    description="Études techniques, génie-conseil et travaux de génie civil par CESA, firme d'ingénierie à Cotonou.",
    eyebrow="Bâtiment",
    hero_title="Génie Civil & <span>Génie-Conseil</span>",
    hero_lead="Une activité de conseil technique transversale, qui appuie chacun de nos domaines d'intervention.",
    intro_paragraphs=[
        "Au-delà de l'installation d'équipements, CESA est sollicitée pour des prestations de génie-conseil et de consultation sur des projets publics et privés : études techniques, dimensionnement, assistance à maîtrise d'ouvrage.",
        "CESA réalise également des travaux de génie civil liés à ses installations techniques (locaux techniques, massifs, tranchées, supports), et assure le suivi et la supervision de chantiers.",
    ],
    intro_bullets=[
        "Études techniques et génie-conseil sur vos projets",
        "Assistance à maîtrise d'ouvrage",
        "Travaux de génie civil liés aux installations techniques",
        "Suivi et supervision de chantiers",
    ],
    badge_text="Conseil technique transversal",
    image=IMG("expertises", "genie-civil-photo.jpg"),
    feature_cards=[
        {"icon": "graduate", "title": "Génie-conseil", "text": "Études techniques et consultation sur vos projets d'ingénierie."},
        {"icon": "crane", "title": "Génie civil", "text": "Travaux liés aux installations techniques et locaux dédiés."},
        {"icon": "award", "title": "Supervision", "text": "Suivi de chantier et assistance à maîtrise d'ouvrage."},
    ],
)

# ============================================================ RÉALISATIONS =
add({
    "slug": "realisations.html",
    "template": "inner",
    "title": "Nos Réalisations",
    "description": "Aéroport International de Cadjehoun, Présidence de la République, éclairage d'axes routiers : les réalisations de CESA au Bénin.",
    "nav_active": "realisations",
    "hero": {
        "image": IMG("hero", "realisations.svg"),
        "breadcrumb": [("Accueil", "index.html"), ("Réalisations", "realisations.html")],
        "eyebrow": "Nos réalisations",
        "title": "Des projets qui <span>parlent</span> pour nous",
        "lead": "De l'aéroport de Cadjehoun à la Présidence de la République, un aperçu des interventions menées par CESA au Bénin.",
    },
    "sections": [
        {
            "type": "split", "id": "siege",
            "eyebrow": "Notre siège",
            "title": "Un ancrage <span>local</span>, à Akpakpa",
            "paragraphs": [
                "CESA opère depuis son siège d'Akpakpa, à Cotonou, d'où ses équipes techniques interviennent sur l'ensemble du territoire béninois.",
            ],
            "image": BUILDING_PHOTO,
            "badge": {"icon": "pin", "text": "Akpakpa, Cotonou"},
        },
        {
            "type": "category-grid", "bg": "alt", "cols": 3,
            "eyebrow": "Projets phares",
            "title": "Quelques repères <span>parmi nos interventions</span>",
            "cards": [
                {"image": IMG("realisations", "aeroport-arrivee-2012.jpg"), "tag": "Infrastructure · 2012", "title": "Extension du Hall Arrivée, Aéroport Cardinal Bernardin Gantin", "text": "Climatisation et électricité pour l'extension du hall des arrivées de l'aéroport de Cotonou.", "href": "climatisation.html"},
                {"image": IMG("realisations", "aeroport-depart-2020.jpg"), "tag": "Infrastructure · 2020", "title": "Extension du Hall Départ, Aéroport Cardinal Bernardin Gantin", "text": "Climatisation et aménagements techniques pour l'extension du hall des départs.", "href": "climatisation.html"},
                {"image": IMG("realisations", "cdpa-siege-2013.jpg"), "tag": "Tertiaire · 2013", "title": "Siège de CDPA", "text": "Électricité bâtiment et réseaux techniques pour la tour du siège de CDPA à Cotonou.", "href": "electricite.html"},
                {"image": IMG("realisations", "upp-solaire-1mw-2018.jpg"), "tag": "Énergie · 2018", "title": "Centrale solaire de 1 MW, Usine UPP", "text": "Conception et installation d'une centrale photovoltaïque industrielle de 1 MW.", "href": "energie-solaire.html"},
                {"image": IMG("realisations", "bid-villages-solaires.jpg"), "tag": "Énergie", "title": "Électrification solaire de 24 villages (BID)", "text": "Installation de kits solaires et d'éclairage public pour 24 villages, financée par la BID.", "href": "energie-solaire.html"},
                {"image": IMG("realisations", "presidence.jpg"), "tag": "Institutionnel", "title": "Présidence de la République", "text": "Prestations techniques pour un site institutionnel de premier plan.", "href": "contact.html"},
                {"image": IMG("realisations", "eclairage-solaire-routier.jpg"), "tag": "Éclairage public", "title": "Éclairage solaire d'axes routiers", "text": "Conception et installation de l'éclairage solaire de plusieurs axes routiers.", "href": "electricite.html"},
            ],
        },
        {
            "type": "cta-banner",
            "title": "Un projet similaire à nous confier ?",
            "text": "Parlez-nous de votre site et de vos contraintes techniques.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
            "secondary": {"label": "Voir nos références", "href": "references.html"},
        },
    ],
})

# ============================================================ RÉFÉRENCES ===
add({
    "slug": "references.html",
    "template": "inner",
    "title": "Nos Références Clients",
    "description": "ASECNA, BGFI, Ecobank, BOA, UNICEF, Gouvernement du Bénin : les références clients de CESA au Bénin.",
    "nav_active": "references",
    "hero": {
        "image": IMG("hero", "references.svg"),
        "breadcrumb": [("Accueil", "index.html"), ("Références", "references.html")],
        "eyebrow": "Nos références",
        "title": "Ils nous font <span>confiance</span>",
        "lead": "Banques, institutions publiques, organisations internationales et entreprises industrielles : un aperçu de nos clients au Bénin.",
    },
    "sections": [
        {
            "type": "clients",
            "eyebrow": "Nos partenaires et clients",
            "title": "Une clientèle <span>institutionnelle</span> et privée",
            "logos": CLIENT_LOGOS,
            "more": CLIENTS_MORE,
        },
        {
            "type": "feature-grid", "bg": "alt", "cols": 4,
            "eyebrow": "Secteurs servis",
            "title": "Des secteurs <span>variés</span>",
            "cards": SECTORS,
        },
        {
            "type": "cta-banner",
            "title": "Rejoignez nos références",
            "text": "Confiez-nous l'étude et la réalisation de votre prochain projet technique.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
            "secondary": {"label": "Nos expertises", "href": "expertises.html"},
        },
    ],
})

# ============================================================ CONTACT ======
add({
    "slug": "contact.html",
    "template": "contact",
    "title": "Contact",
    "description": "Contactez CESA à Akpakpa, Cotonou, pour vos projets d'énergie, d'électricité, de climatisation ou de sécurité.",
    "nav_active": "contact",
    "hero": {
        "image": IMG("hero", "contact.svg"),
        "breadcrumb": [("Accueil", "index.html"), ("Contact", "contact.html")],
        "eyebrow": "Contact",
        "title": "Parlons de <span>votre projet</span>",
        "lead": "Une question, un devis, un projet technique ? Nos équipes vous répondent rapidement.",
    },
})
