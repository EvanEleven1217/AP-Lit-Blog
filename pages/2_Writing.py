import streamlit as st
import base64
from PIL import Image

st.title("Writing")

st.caption("Indenting/Formatting does not work, please disregard.")
st.caption("Please be patient if any tabs are not loading.")

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

            \n\r Initially, I imagined I would mostly be completing service hours 
            and bonding with kids; however, over time, I realized that the 
            value within was far more substantial. Each of my service days 
            was filled with kids who were passionate about STEM, sometimes 
            so passionate that they would disobey their parents to stay 
            longer. As I watched their excitement, I was reminded of the 
            times when I was in their shoes, so eager to learn. Eventually, 
            this realization motivated me to mentor kids with the same spirit 
            of excitement. 

            \n\r DC’s motto is “Inspire. Educate. Impact.” With dedication, I 
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

            \n\r My time at DC has shown me that leadership is more than a title. 
            As I prepare to apply for the captain position, I look forward 
            to taking on greater responsibilities and serving others more 
            effectively. To all guests, staff, and volunteers, I leave 
            behind a profound effect that models the motto, and as time 
            progresses, I hope that my leadership will influence others 
            to also inspire, educate, and impact.
            """)
        
    st.subheader("About Me")
    image = Image.open('me.png')
    st.image(image)

with st.expander("November"):

    st.subheader("Fences Analysis")
    st.write("""
            In Fences by August Wilson, he employs the symbol of fences to depict 
            that family relationships should be protected inside and out. Throughout 
            the play, there are literal and figurative fences that tear the Maxson 
            family apart. Ironically, destruction is the opposite of what they wished 
            for. For example, Rose Maxson, the main character’s wife, has Troy, the 
            main character, build a fence around their house to keep love within her 
            family and be “[protected] as [they] go on [their] way.” In this instance, 
            Rose’s desire for social safety emerges because the fence separates her 
            family from the racial discrimination in society. As the play progresses, 
            the fence shifts to symbolize the conflict between Troy and his son, Cory. 
            Cory’s dream is to play football, but Troy demands that Cory quit football 
            and work a stable job because of “what [people] did to [Troy] in sports.” 
            Cory is upset at Troy’s order because football is his only passion, and 
            this disagreement creates tension that eventually forms a “fence” between 
            Troy and Cory. As a result, future arguments are sparked, leading to 
            Cory’s ultimate avoidance of Troy. On the other hand, another “fence” 
            is established when Troy reveals to Rose that he had an affair. Having 
            spent 18 years of her life “[burying her feelings] inside Troy,” Rose is 
            devastated upon the news, and her intentions of nurturing her family die. 
            Rose, being disappointed, talks to Cory about the situation, only to hear 
            that Cory is also disappointed in Troy but for different reasons. Cory 
            claims that Troy does“nothing but hold [him] back” in life because Troy 
            doesn’t let him pursue his dreams. The already existing “fence” between 
            Troy and Cory thickens when Cory encounters Troy sitting on the doorstep. 
            As Cory walks around Troy to go inside, tension arises because Troy 
            believes that Cory is disrespecting him by not acknowledging him. As 
            the tension grows, Cory eventually walks away and says that he’ll be 
            back for his things, and in response, Troy tells Cory that his stuff 
            will be “on the other side of [the] fence.” Kicking Cory out of the house 
            depicts Troy as powerful and territorial because he is able to choose who 
            stays and who goes. Cory is irritated that Troy acts as the highest 
            authority in the house given that Troy used Uncle Gabe’s money to buy 
            it, and he escalates the situation further by confronting him about how 
            he doesn’t truly own the house. Cory’s confrontation leads to an even 
            thicker “fence” that prompts Cory not to attend Troy’s funeral after 
            his passing. In the end, the Maxson family becomes shattered into pieces 
            as a result of fences. All in all, Wilson utilizes fences to depict that 
            a boundary may deter outside destruction, but it may discretely cultivate 
            inner destruction.
            """)


    st.subheader("UC Prompt 6")
    st.write("""
            I love technology. 
	        \n\r When I say that, it’s to an unimaginable extent. Hardware? Software? 
            All technological innovations fascinate and inspire me to contribute 
            to the next generational development. Over the past seven years, I 
            have been cultivating this passion; in fact, my curiosity for technology 
            has never been stronger.

            \n\r Software. My programming foundation developed in middle school when I 
            enrolled in an introductory game development class. I was thrilled that 
            I created a functioning game with coding blocks, and it motivated me to 
            learn real programming languages, hence why in high school, I enrolled 
            in my first programming class: C# game development. My understanding of 
            C# confirmed my interest in programming. Consequently, I enrolled in AP 
            Computer Science A (APCS-A), which became the keystone of my programming 
            knowledge. Learning Java and applying it to solve real-life problems that 
            would otherwise take a human an eternity to solve was where I realized 
            the importance of programming. Upon completing APCS-A, there was no 
            higher-level course, so I had to pursue my interests independently. I 
            researched for a class that would succeed APCS-A, and I settled on a Python 
            specialization course that covered the basics through databases and web data. 
            I loved it. While programming, I reached a mutual understanding with computers: 
            writing special words that only we could interpret.

	        \n\r Hardware. I view hardware as puzzle pieces. When they’re connected properly, 
            they form something revolutionary. I’ve taken apart an iPhone, iPad, and 
            MacBook down to their core and managed to reassemble them, whether for fun 
            or repair. During this process, I was able to view and tinker with the devices’ 
            components: CPU, RAM, motherboard, and more. Using the knowledge I’ve gained, 
            I built two custom computers, component by component. Ultimately, I learned 
            how technology works behind the scenes to create the things people cherish. 
            Connecting this and that makes something else possible. Infinite possibilities 
            await.

            \n\r Friends, family, and non-profit organizations already see me as the 
            “go-to-computer-guy,” and I plan to be that same person for more people. 
            With my interest and determination, I will grow to revolutionize the 
            technology industry and define innovation.
            """)
        
    st.subheader("My PC")
    image = Image.open('PCMindmap.png')
    st.image(image)

with st.expander("December/January"):

    st.subheader("\"Once Upon a Time\" Analysis")
    st.write("""
            In the short story, “Once Upon a Time,” Nadine Gordimer utilizes the symbolism 
            of a gold mine to assert that wealth gaps and stress can lead to a society’s 
            collapse. To begin, the narrator is woken in the middle of the night by creaking 
            sounds coming from her wooden floor. She initially believes the sounds are coming 
            from possible intruders, considering the kind of area she lives in, but she soon 
            concludes that the sounds are a “buckling, an epicenter of stress,” due to a gold 
            mine underneath her house. As a result of the constant excavation, the narrator’s 
            “whole house shifts” due to being strained by physical pressure. This draws a 
            parallel to the narrator’s mental health, which slowly deteriorates by living 
            in an unfair community. Through her views and experiences, she notices that 
            segregation is a leading movement in her community. Some live a luxurious life 
            with housemaids, while some live surrounded by razor thorns. As her house crumbles, 
            so does her faith in society, which illustrates how agony can destroy one’s mindset. 
            Additionally, the shaking symbolizes greed because even though the mining damages 
            houses’ foundations, the mine operators are negligent and put profits over people's 
            quality of life. The shaking creates an “uneasy strain” between the “brick, cement, 
            wood, and glass” of the narrator’s house and separates them, which symbolizes the 
            people in society because they are becoming divided due to the mine operator’s 
            mining orders, or greed. Some people benefit financially through another person’s 
            suffering; thus, wealth gaps encourage a collapse in society. Moreover, the wealth 
            gaps pose another problem: desperate workers in poverty. Chopi and Tsonga, the 
            narrator’s friends, are “migrant” mine employees who risk their lives to make a 
            living regardless of the chance of being “interred there in the most profound of 
            tombs.” With the mine consisting of many structural failures and water ruptures, 
            the workplace symbolizes the workers’ unstable life quality as they try to meet 
            the basic needs in a societal system managed by the rich. Eventually, the burdens 
            will break the workers’ will, resulting in death. As a result of worker deaths, 
            the workforce will decline, which will lead to a collapse of the economy, and 
            eventually, the entire society will crumble. All in all, Gordimer uses the 
            symbolism of a gold mine to demonstrate that wealth gaps and stress can destroy 
            a society.
            """)

    st.subheader("UC Prompt 7")
    st.write("""
            \n\r Vision Youth Charity Center (VYCC) piqued my interest with its mission to play 
            music for those with visual impairments. Because of this specific and powerful 
            mission, I joined VYCC’s orchestra as a viola player. Over time, VYCC has 
            guided me to use my talents–musical and otherwise–to benefit society. 

            \n\r When I joined, I wasn’t sure what my impact would be. What I knew was that I 
            enjoyed the ability to use my musical gifts to introduce a new tone to the 
            orchestra. Each concert reminded me that my years of practice were more than 
            for my personal gain; it was actually being used to bless others. 

            \n\r It’s been four years since I joined, and VYCC has grown in size and structure. 
            With growth came a new mission: to raise funds to help provide shelter and food 
            for North Korean refugees. Once again, I loved how specific the mission was 
            because it gave me insight into what kind of impact I can make. The orchestra 
            became the primary source of funds for the mission, and I was excited to 
            contribute to it.

	        \n\r Wanting to do more, in 2022, I volunteered as VYCC’s secretary. As secretary, 
            I took on a lot of responsibilities, such as organization and giving speeches. 
            As I was getting immersed in the VYCC’s leadership, I also became the webmaster, 
            and I was most eager about this because technology has always been my passion. 
            Using my technological skills and creativity, I now manage VYCC’s website, and 
            I am able to influence how people interact with VYCC and how VYCC reaches out 
            to the world. 

            \n\r Prior to VYCC, I used my knowledge and talents to benefit myself; however, my 
            involvement as a member and staff opened my eyes to use my gifts to help people 
            from all different walks of life. Through VYCC, I created musical memories for 
            those who cannot see and gave North Korean refugees a new chance in life. In 
            the future, VYCC’s mission will transition to helping Mexicans escape poverty, 
            and I will use my gifts to positively change their lives as well.
            """)

    st.subheader("K-Pop")
    image = Image.open('kpop.png')
    st.image(image)

with st.expander("February"):

    st.subheader("\"Out Out\" Analysis")
    st.write('''
            Robert Frost’s poem, “Out Out,” portrays the speaker’s complex attitude about 
            life and death to assert that memories in life can easily fade away. In the 
            beginning, the boy works diligently as he cuts wood with a saw. The speaker 
            wishes that the boy “call it a day” because the speaker recognizes the boy's 
            hard work and wants to express concern for his safety. By showing sympathy 
            for the boy, the speaker illustrates a positive value for life, which 
            potentially outlines the need to cherish and protect life as World War I 
            rages on. Later on in the poem, the boy dies due to a severed hand. 
            Interestingly, the events that succeed the boy’s death contradict the 
            speaker’s stance on life value. For instance, the speaker believed that 
            the boy's death had “no more to build on,” which indicates that the loss 
            had no significant impact. An absence of a reaction from the speaker depicts 
            that the speaker has no attachment to the boy, ultimately contradicting the 
            appreciation of life demonstrated previously. With nothing to say or feel 
            regarding the boy’s death, the speaker moved on as if nothing had happened. 
            Additionally, the speaker’s value of life diminishes further when he “turned” 
            back to “affairs” because the speaker “[was] not the one dead.” Through the 
            speaker’s self-centered response, Frost conveys that those who die fade from 
            memory. Survivors live for themselves and leave others behind. All in all, 
            the speaker employs a complex attitude about life and death to convey that 
            the outcome of life remains unpredictable, and memories of the dead will 
            not linger.
            ''')

    st.subheader("Coding in a Nutshell")
    st.caption("Three lines are one stanza. I couldn't get it to format properly.")
    st.write("""
            \n\rA code script.
            \n\r30 lines on show,
            \n\rOrganized, yet complicated.
            \n\r
            \n\rFor each line:
            \n\rNo syntax errors.
            \n\rAll seems well.
            \n\r
            \n\rThe script executes,
            \n\rAnd hope dies
            \n\rDue to a list of bugs.
            \n\r
            \n\rFor bug in bugs:
            \n\rStuck in a loop.
            \n\r“i” is not changing.
            \n\r
            \n\rTo break out,
            \n\r“i” must increment.
            \n\rSo new code gets typed.
            \n\r
            \n\rThe script executes,
            \n\rAnd hope dies
            \n\rDue to a list of bugs.
            \n\r
            \n\rFor bug in bugs:
            \n\rRun-time errors originate
            \n\rOn line 20.
            \n\r
            \n\rOperations on incompatible types
            \n\rcannot function,
            \n\rSo new code gets typed.
            \n\r
            \n\rWhile bugs has bug:
            \n\rGoogle to find a fix.
            \n\rHours on Stack Overflow.
            \n\r
            \n\rIf bugs is None:
            \n\rJoy gets declared and initialized,
            \n\rAnd never mutated.
            """)

    st.subheader("Apple Products")
    image = Image.open('appleProducts.png')
    st.image(image)
    
with st.expander("March"):
    st.subheader("Nothing here as of now!")

with st.expander("April"):
    st.subheader("Nothing here as of now!")





