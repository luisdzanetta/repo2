import streamlit as st

#Título da página
st.title("Cálculo do MDE")

#Descrição do título da página
st.write("O **MDE**, é o tamanho mínimo da diferença entre as taxas de conversão das variantes e do grupo de controle que pode ser detectado com um nível de significância alpha e um poder de teste beta. Em outras palavras, se a diferença entre as taxas de conversão das variantes e do grupo de controle for menor que o MDE, não será possível detectar essa diferença com um nível de significância alpha e um poder de teste beta especificados.")

#Equação para cálculo do MDE mudança a igualdade
st.write("**Equação para cálculo do MDE**")
st.write("A equação do Mínimo Tamanho Detectável do Efeito (MDE) é:")
st.latex(r'''\text{MDE} = \sqrt{\frac{1}{p-1} \div \frac{n}{16}}''')
st.write("**Onde:**")
st.write("**p:** É a conversão base do controle")
st.write("**n:** É a amostra por variante, considerando distribuição proporcional")

#Equação original, cálculo do n (Kohav et al., 2009)
st.write("**A equação apresentada anteriormente é um derivação da seguinte equação:**")
st.latex(r'''n = \frac{16 \sigma^2}{\Delta}''')
st.write("**Onde:**")
st.write("**σ:** É a variância, adaptada para distribuição de Bernoulli")
st.write("**Δ:** É a amostra por variante, considerando distribuição proporcional")

st.divider()

st.write("**Referência:**")

st.download_button('Baixar o artigo', "https://link.springer.com/content/pdf/10.1007/s10618-008-0114-1.pdf?pdf=button", file_name="Kohav et al. (2009)_Controlled experiments on the web: survey and practical guide")
st.image("https://raw.githubusercontent.com/luisdzanetta/repo2/main/kohav.png")


        
