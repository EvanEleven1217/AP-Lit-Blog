import streamlit as st
import base64

st.title("Writing")

st.caption("Indenting/Formatting does not work, please disregard.")

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

with st.expander("October"):

    st.subheader("“Introduction to Poetry” Analysis")
    st.write("""
            Billy Collins' poem, “Introduction to Poetry,” 
            is packed with auditory, visual, and tactile imagery to convey 
            that poetry is often much easier to analyze than anticipated. 
            Throughout the poem, the speaker outlines an analytical process 
            and discusses the simplicity within. As a starting point, when 
            the speaker instructs the readers to listen to “[the poem’s] hive,” 
            auditory imagery emerges because a bee hive contains thousands of 
            bees that all contribute toward the hive (Collins, stanza 2). 
            This illustration creates an analogy between a hive and a poem, 
            which is then used to persuade readers to take a poem’s words as 
            a whole, not individually. Only by listening to the poem's full 
            story will one discover its meaning. Secondly, visual imagery can 
            be noticed when the speaker advises to deposit a “mouse into a poem” 
            and observe it “probe [its] way out” (Collins, stanza 3). The 
            example of a mouse mindlessly weaving its way out of the maze 
            over time mimics readers’ possible experiences with poems: read 
            and derive their meaning in time. Mazes require patience, trial, 
            and error, similar to the requirements of analyzing a poem, so 
            if readers dedicate all three, they will uncover the meaning. 
            Lastly, tactile imagery can be witnessed when “[walking] inside 
            the poem’s room” (Collins, stanza 4). Here, the poem is 
            characterized as a room, and readers must “feel the walls for 
            a light switch” (Collins, stanza 4). In this instance, it appears 
            that readers can feel blindly indulged in a poem’s story; however, 
            readers will eventually identify the meaning because there are 
            only so many words to process. Moreover, the demonstration proves 
            that one must have the basic knowledge to analyze a poem. 
            To find a light switch in a dark room, one must feel the walls 
            rather than the ground, and poems are no different, one must 
            know which words are more significant than others. Imagery is a 
            valuable commodity to Collin in his attempt to convey to the 
            readers that reading with an open mind and patience is the key 
            to analyzing a poem. 
            """)

    st.subheader("UC Prompt 1")
    st.write("""
            As a kid, I often went to Discovery Cube (DC). During my 
            visits, I recall being mesmerized by the aerodynamics chamber 
            with winds blowing 90 mph and the dino quest station where I 
            scavenged for fossils. Through stations like these, the staff 
            helped me learn STEM fundamentals in memorable ways, which 
            ultimately influenced my career path. To return the favor 
            and thank DC for shaping my interests, I became a volunteer to 
            influence the future generation.

            Initially, I imagined I would mostly be completing service hours 
            and bonding with kids; however, over time, I realized that the 
            value within was far more substantial. Each of my service days 
            was filled with kids who were passionate about STEM, sometimes 
            so passionate that they would disobey their parents to stay 
            longer. As I watched their excitement, I was reminded of the 
            times when I was in their shoes, so eager to learn. Eventually, 
            this realization motivated me to mentor kids with the same spirit 
            of excitement. 

            DC’s motto is “Inspire. Educate. Impact.” With dedication, I 
            strive to model each aspect of the motto. Inspire: by 
            demonstrating intriguing experiments like chromatography 
            and sound waves, I provide first-hand experiences that make 
            science enjoyable. Educate: by discussing the STEM concepts 
            that apply to these experiments, I guide every kid, regardless 
            of age, to understand each concept through easy terminology. 
            Impact: by training in multiple volunteer branches and offering 
            guests a surreal experience, I leave a lasting impression. 
            Moreover, my commitment to a weekly schedule manifests my reliability, 
            which is favorable to staff and volunteers; therefore, I 
            impact DC holistically.

            My time at DC has shown me that leadership is more than a title. 
            As I prepare to apply for the captain position, I look forward 
            to taking on greater responsibilities and serving others more 
            effectively. To all guests, staff, and volunteers, I leave 
            behind a profound effect that models the motto, and as time 
            progresses, I hope that my leadership will influence others 
            to also inspire, educate, and impact.
            """)

with st.expander("November"):
    st.subheader("Coming soon!")

with st.expander("December"):
    st.subheader("Nothing here as of now!")

with st.expander("January"):
    st.subheader("Nothing here as of now!")

with st.expander("February"):
    st.subheader("Nothing here as of now!")

with st.expander("March"):
    st.subheader("Nothing here as of now!")

with st.expander("April"):
    st.subheader("Nothing here as of now!")

with st.expander("May"):
    st.subheader("Nothing here as of now!")

with st.expander("June"):
    st.subheader("Nothing here as of now!")



