import streamlit as st
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
def show():
    st.markdown("""
    <style>
    /* Conteneur général */
    .stApp {
        background-color: #f4f4f9;
        font-family: 'Arial', sans-serif;
        color: #333;
        padding: 2rem;
    }

    /* Titre principal */
    h1 {
        text-align: center;
        font-size: 3.5em;
        color: #fffff;
        font-weight: bold;
    }

    /* Sous-titre */
    h2 {
        color: #fffff;
        text-align: center;
        margin-top: 20px;
        font-size: 2em;
    }
    /* Sous-sous-titre */
    h3 {
        color: #333;
    }

    /* Card style pour les sections */
    .card {
        background-color: #fff;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
    }
    .card:hover {
        transform: translateY(-10px);
    }

    /* Boutons élégants */
    .btn {
        display: inline-block;
        background-color: #fffff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: 2px solid #0056b3; 
        text-decoration: none;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }

    .btn:hover {
        background-color: #0056b3;
    }

    /* Alignement des liens */
    .links {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }

    /* Footer élégant */
    footer {
        text-align: center;
        margin-top: 40px;
        font-size: 0.8em;
        color: #666;
        border-top: 1px solid #ddd;
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Ajouter une photo
   

    # Titre principal
    st.markdown("<h1>Tom Heising étudiant à Efrei Paris</h1>", unsafe_allow_html=True)
    
 # Charger l'image depuis le fichier local
    #image = Image.open("/Users/tomheising/Desktop/Data Vizualisation Project /Data/IMG_6696.jpg")

    # Redimensionner l'image
    #image = image.resize((150, 150))

    # Créer un masque pour le cercle
    #mask = Image.new('L', image.size, 0)
    #draw = ImageDraw.Draw(mask)
    #draw.ellipse((0, 0) + image.size, fill=255)

    # Appliquer le masque à l'image
    #output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    #output.putalpha(mask)

    # Afficher l'image avec Streamlit et l'aligner au centre
    #st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    #st.image(output, caption='', width=200)
    #st.markdown("</div>", unsafe_allow_html=True)

    # Sous-titre
    st.markdown("<h2>Étudiant en Data Science/Business Intelligence</h2>", unsafe_allow_html=True)

    # Section "À propos de moi"
    st.markdown("""
        <div class="card">
            <h3>À propos de moi &#128104;&#8205;&#128187;</h3>
            <p>
            Passionné par l'innovation et les données, je me spécialise en Data Science et en Business Intelligence. Avec de solide connaisances en analyse de données, modélisation et visualisation, 
            j'ai contribué à des projets variés allant de l'analyse prédictive à l'analyse pur et dur de données.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Section "Compétences"
    st.markdown("""
        <div class="card">
            <h3>Compétences clés &#128187;</h3>
            <ul>
                <li>Python (Pandas, NumPy, Scikit-learn, TensorFlow)</li>
                <li>Data Visualization (Matplotlib, Seaborn, Plotly, Folium, Power BI, Altair)</li>
                <li>Machine Learning & AI (modélisation, hyperparameter tuning)</li>
                <li>Business Intelligence</li>
                <li>SQL, NoSQL, gestion de bases de données</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    #Section "Soft Skills"
    st.markdown("""
        <div class="card">
            <h3>Soft Skills &#128104;</h3>
            <ul>
                <li>Esprit analytique</li>
                <li>Créativité</li>
                <li>Curiosité</li>
                <li>Esprit d'équipe</li>
                <li>Adaptabilité</li>
                <li>Communication</li>
                <li>Aisance à l'orale</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Section "Expérience"
    st.markdown("""
        <div class="card">
            <h3>Mon expérience &#128188;</h3>
            <p>
            Je possède une expérience scolaire approfondie dans la Data Science et de la Business Intelligence grâce à divers projets académiques, où j'ai eu l'opportunité de travailler sur des projets comprenants de grands datasets, et qui m'ont permis d'apprendres des techniques de data cleaning et de machine learning avancées. Afin de proposer une ou plusieurs solutions intéressantes au problèmes posés.
            et des infrastructures de données complexes.
            </p>
            <p>
            D'un point de vue purement professionnel je n'ai pas encore eu l'opportunité de travailler dans la data science, toutefois j'ai déjà eu plusieurs expériences professionnel notamment chez Nespresso où j'ai travaillé en tant que vendeur ployvalent.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Section "Projets"
    st.markdown("""
        <div class="card">
            <h3>Projets récents &#128202;</h3>
            <ul>
                <li><a href="https://github.com/0adri3n/pronobo" class="btn" target="_blank">Pronobo</a></li>
                <li><a href="https://github.com/arthur-gtgn/TRBF" class="btn" target="_blank">TRBF Project</a></li>
                <li><a href="https://github.com/arthur-gtgn/Data-Master-Project/tree/main" class="btn" target="_blank">Immo analysis project</a></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Section "Liens professionnels"
    st.markdown("""
        <div class="card">
            <h3>Mes profils professionnels &#128084;</h3>
            <div class="links">
                <a href="https://www.linkedin.com/in/tom-heising-383977222/" class="btn" target="_blank">LinkedIn</a>
                <a href="https://publuu.com/flip-book/692844/1541235" class="btn" target="_blank">Mon CV</a>
                <a href="mailto:tom.heising@efrei.net" class="btn">Contactez-moi !</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <footer>
            <p>© 2024 - Tom Heising | Votre prochain Data analyst | <a href="mailto:tom.heising@efrei.net">Contactez-moi</a></p>
        </footer>
    """, unsafe_allow_html=True)