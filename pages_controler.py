import streamlit as st
import pages.projetos.home as home
import pages.projetos.projeto01 as PageProjetos01
import pages.projetos.projeto02 as PageProjetos02
import pages.projetos.papers as papers
import pages.projetos.sprints as sprints
import pages.projetos.publica as publica

pj0 = "Home"
pj1 = "Experiment 01"
pj2 = "Experiment 02"
pj3 = "Publications"
pj4 = "Publication in production"


st.sidebar.title('Menu')
page_projeto = st.sidebar.selectbox('Escolha um página de interesse',
                                    [pj0, pj1, pj2, pj3, pj4])

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**Coordinator**: [Danilo Andrade](https://daniloas.com/)')
st.sidebar.markdown('**Supervisor**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
st.sidebar.markdown('**Technical support**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
st.sidebar.markdown('**Junior Researcher**: Mateus Hastenreiter')
st.sidebar.markdown('**Junior Researcher**: Maria Eduarda')
st.sidebar.markdown('**Junior Researcher**: Aurélio Martins')


def Choice():
    if page_projeto == pj0:
        home.home()

    elif page_projeto == pj1:
        PageProjetos01.Projeto01()

    elif page_projeto == pj2:
        PageProjetos02.Projeto02()

    elif page_projeto == pj3:
        papers.papers()

    elif page_projeto == pj4:
        sprints.sprints()

Choice()