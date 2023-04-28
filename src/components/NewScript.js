import React from 'react'
import {TwitterIcon, FacebookIcon, LinkedinIcon, RedditIcon} from "react-share"
import {TwitterShareButton, FacebookShareButton, LinkedinShareButton, RedditShareButton, FacebookShareCount} from "react-share"



function NewScript() {

        let scripts = [{"name": "For this is the whole duty of man, that we fear Yah and keep his commandments and his commandments are not grievous.",  
                        "chapter": "Ecclesiastes 12:13",
                        "action": "Read Exodus 20 and find at least two commandments you can do better with"}, 
                        {"name": "Sin is the transgression of the law",  
                        "chapter": "1 John 3:4",
                        "action": "Read a chapter from the book of Deuteronomy and try to find a law you are not currently aware of."},
                        {"name": "For this is the love of Yah, that we keep his commandments",  
                        "chapter": "1 John 5:3",
                        "action": "How can we show Yah that we love him more today?",
                        },
                        {"name": "We shall not live by bread alone, but by every word that proceeds from Yah",  
                        "chapter": "Luke 4:4",
                        "action": "Go back into the Torah (Genesis-Deuteronomy) and find some of Yah's words that you may not be familiar with.",
                        },
                        {"name": "Humble yourselves therefore under the mighty hand of Elohim, that he may exalt you in due time:",  
                        "chapter": "1 Peter 5:6",
                        "action": "How can you show more humility today?",
                        },
                        {"name": "Have not I commanded thee? Be strong and of a good courage; be not afraid, neither be thou dismayed: for the Yah your Elohim is with thee whithersoever thou goest.",  
                        "chapter": "Joshua 1:9",
                        "action": "When was the last time you didnt show courage? How can you change that next time?",
                        },
                        {"name": "Blessed are they that keep his testimonies, and that seek him with the whole heart.",  
                        "chapter": "Psalms 119:2",
                        "action": "How can you seek Yah more today?",
                        },
                        {"name": " I remembered thy judgments of old, O Yah; and have comforted myself.",  
                        "chapter": "Psalms 119:52",
                        "action": "What is one of Yah's wonders that you can think about to comfort yourself?",
                        },
                        {"name": "I thought on my ways, and turned my feet unto thy testimonies.",  
                        "chapter": "Psalms 119:59",
                        "action": "What is one way you can turn your feet back to the testimonies of Yah?",
                        },
                        {"name": "I made haste, and delayed not to keep thy commandments.",  
                        "chapter": "Psalms 119:60",
                        "action": "Have you been delaying to keep Yah's commandments? Why or why not?",
                        },
                        {"name": "The law of thy mouth is better unto me than thousands of gold and silver.",  
                        "chapter": "Psalms 119:72",
                        "action": "Which one is more important to you: The Torah (Law) of Yah or money?",
                        },
                        {"name": "Depart from me, ye evildoers: for I will keep the commandments of my God.",  
                        "chapter": "Psalms 119:115",
                        "action": "Who is someone around you that you need to depart from you in order for you to grow?",
                        },
                        {"name": "My flesh trembleth for fear of thee; and I am afraid of thy judgments.",  
                        "chapter": "Psalms 119:120",
                        "action": "Are you afraid of Yah's righteous judgements according to the Torah?",
                        },
                        {"name": "I thought on my ways, and turned my feet unto thy testimonies.",  
                        "chapter": "Psalms 119:59",
                        "action": "What is one way you can turn your feet back to the testimony of Yah?",
                        },
                        {"name": "I hate and abhor lying: but thy law do I love.",  
                        "chapter": "Psalms 119:163",
                        "action": "When was the last time you lied? Why?",
                        },
                        {"name": "For whosoever shall keep the whole law, and yet offend in one point, he is guilty of all.",  
                        "chapter": "James 2:10",
                        "action": "Find a law you are not keeping a make an action plan to keep it today.",
                        },
                        {"name": "Can the fig tree, my brethren, bear olive berries? either a vine, figs? so can no fountain both yield salt water and fresh",  
                        "chapter": "James 3:12",
                        "action": "Read this scripture carefully. How is this being exemplified in your life?",
                        },
                        {"name": "This wisdom descendeth not from above, but is earthly, sensual, devilish.",  
                        "chapter": "James 3:15",
                        "action": "Is some of the wisdom you are holding onto earthly? What is the heavenly alternative?",
                        },
                        {"name": "For where envying and strife is, there is confusion and every evil work.",  
                        "chapter": "James 3:16",
                        "action": "How can you eliminate envying and strife in your life?",
                        },
                        {"name": "Submit yourselves therefore to Elohim. Resist the devil, and he will flee from you.",  
                        "chapter": "James 4:7",
                        "action": "How can you resist the devil today to cause him to flee from you?",
                        },
                        {"name": "Humble yourselves in the sight of Yahuah, and he shall lift you up.",  
                        "chapter": "James 4:10",
                        "action": "Name 2 ways you can minimize your pride and humble yourself before Yah?",
                        },
                        {"name": "I thought on my ways, and turned my feet unto thy testimonies.",  
                        "chapter": "Psalms 119:59",
                        "action": "What is one way you can turn your feet back to the testimonies of Yah?",
                        },
                        {"name": "Therefore to him that knoweth to do good, and doeth it not, to him it is sin.",  
                        "chapter": "James 4:17",
                        "action": "Familiarize yourself with Leviticus and Deuteronomy to become more aware of Yah's laws.",
                        },
                        {"name": "Then Yahushua said unto them, 'Yet a little while is the light with you. Walk while ye have the light, lest, darkness come upon you; for he that walks in darkness knows not where he goes'",  
                        "chapter": "John 12:35",
                        "action": "We know that the commandments are a lamp, and the Torah (Law) is the light. Let's let those guide us in darkness.",
                        },
                        {"name": "For Yahuah your Elohim is he that goes with you, to fight for you against your enemies, to save you.",  
                        "chapter": "Deuteronomy 20:4",
                        "action": "Remember that Yah is with you, if you keep his commandments. Trust that he will fight your battles for you.",
                        }]

                        let num = Math.floor(Math.random() * scripts.length)
        return (
        <div className="flex items-center justify-center flex-col">
             {/*Scripture Verse*/}
            <div className="w-full flex h-auto mb-4 rounded-lg p-2 flex-col border-gray-50 text-center">
                <h1 id="text" className="text-2xl font-bold mb-2"> {scripts[num].name}</h1> 
                <h4 id="location" className="text-sm">{scripts[num].chapter}</h4>
            </div>
            {/*Share*/}
            <div className="space-x-4 mt-4 flex w-full justify-center items-center">
                <FacebookShareButton
                url="https://yahdaily.vercel.app/"
                quote={scripts[num].name + " (" + scripts[num].chapter + ")" + " | " + scripts[num].action}
                title="My Daily Scriptures"
                className="Demo__some-network__share-button">
                    <FacebookShareCount url="https://yahdaily.vercel.app/" />
                    <FacebookIcon
                    size={32}
                    round />
                </FacebookShareButton>
                <TwitterShareButton
                url="https://yahdaily.vercel.app/"
                className="Demo__some-network__share-button">
                    <TwitterIcon
                    size={32}
                    round />
                </TwitterShareButton>
                <LinkedinShareButton
                url="https://yahdaily.vercel.app/"
                summary={scripts[num].name}
                source="Daily Scripture Generator"
                className="Demo__some-network__share-button">
                    <LinkedinIcon
                    size={32}
                    round />
                </LinkedinShareButton>
                <RedditShareButton
                url="https://yahdaily.vercel.app/"
                summary={scripts[num].name}
                source="Daily Scripture Generator"
                className="Demo__some-network__share-button">
                    <RedditIcon
                    size={32}
                    round />
                </RedditShareButton>
            </div>

            {/*Action*/}
            <div className="w-full md:w-3/4 justify-center text-sm rounded-lg bg-blue-50 mt-4 shadow-inner hover:border-blue-300 transition border-2 border-transparent flex p-2 flex-col text-center">
                <h4 className=" justify-center italic px-2 md:px-8" id="action">{scripts[num].action}</h4>
            </div>
        </div>
    )}


export default NewScript
