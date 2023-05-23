import streamlit as st
import base64

st.title("Other")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('mountainBackground.jpg') 

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if st.text_input("Check Sticky Note") == "C7rP-8qK2":
    with st.expander("2023 Final Blog Reflection"):
        
        st.caption("Indenting/Formatting does not work, please disregard.")
        st.write("""
                Dear Mrs. St. Amant,

                Me, myself, and I. These are the only people I had during my senior 
                year of high school. Never before have I experienced this level of 
                loneliness in my life, and it destroyed my mentality for the year. 
                High school wasn't always bad, it was fine until the second semester 
                of senior year. If I had to rank all my years from best to worst, it 
                would be sophomore year, freshman year, junior year, and last and 
                least, senior year. I wish I could write a positive reflection letter, 
                but that’s simply not possible with my current mentality. I’m barely 
                hanging on at the lowest point in my life. Whenever someone asks 
                “How are you” or “Are you okay,” my first thought is “Do I lie and 
                say I’m fine, or do I just spill.” Usually, I resorted to lying 
                because I’ve accepted my situation. Because this reflection will 
                be published on the internet, I don’t wish to elaborate as to why 
                I’m in this state, but in a nutshell, all my problems stemmed from 
                loneliness. My fear of being left out most definitely did not help 
                either. But like I said, I’ve accepted my situation, and this 
                lifestyle is my norm, at least for now. Hopefully, my future doesn’t 
                look this dark; I already planned out how to shape my life in college, 
                so I’ll start fresh and happy again. It sounds generic, but in college, 
                I plan on getting involved in as many activities as possible so that 
                I can develop connections. As for the end of this school year, I look 
                forward to graduation for all the wrong reasons: I won’t have to see 
                anyone after the ceremony and I can truly put everything behind my back. 
                Three weeks of school left, then I’m free from my misery. Okay, enough of 
                this sad talk, I’ll move on to the positive things. All the previous 
                talk was about my in-person life, but my online life looks different. 
                Video games serve as my escape from reality, not because of the gameplay 
                itself, but because the platform acts as a portal for me to make friends 
                online. I’ve gotten close to several amazing people, and they offer me 
                more peace and company than most people in real life, so I thank these 
                people for supporting me during my darkest times.

                Writing. I never saw myself as a strong writer; I’m more of a math 
                and science-sided person. Regardless, I improved my writing skills 
                this year. Similar to AP Lang, the revision process for writing pieces 
                helped me learn from my mistakes and seek solutions. Without a doubt, 
                my writing stands nowhere near perfection, and it never will because 
                it’s not an area I have an interest in. Personally, I’d rather write 
                code for the next generation of AI software, lol. Anyways, one of 
                my weaknesses in AP Lit was providing insightful commentary. I 
                received “dig deeper” comments on many of my essays, and I always 
                spent a good chunk of time staring at the passage trying to think 
                of more things I can dissect. And usually, I just chose some random 
                BS that I can talk about, wrote a few extra sentences, and eventually 
                you gave me a final. It felt like I was getting off the hook easily 
                and getting finals on my pieces, but now I realize this process 
                embodies the entire point of the revision process. Whether I elaborate 
                on something valuable or not, the ability to decipher something 
                beyond its face value is the skill that you wanted to instill in 
                my life. Another weakness I had was a lack of creativity. For some 
                pieces, especially mind maps and poems, I lacked thought. One of 
                my poems, “What Should the Title Be,” demonstrates my lack of 
                creativity. Although the poem itself ended up creative, it addresses 
                a problem that I had: not being creative. That day, I couldn’t think 
                of a topic for my poem, and I sat there for a while before realizing 
                that I could turn my problem - the inability to come up with a topic 
                \- into my solution: a description of my dilemma. Thanks to this 
                writing piece, I realized that how I choose to approach a problem 
                makes all the difference.

                And just like that, the school year nears its end. I learned many 
                lessons this year, whether about life or writing. Although it was a 
                shitty year (this word most accurately depicts my experience, please 
                excuse me), the lessons I learned will live on in my memories and 
                guide me in my future endeavors. Thank you, Mrs. St. Amant.

                Best regards,

                Evan Lee
                """)
                
