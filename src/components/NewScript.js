import React, { useState, useEffect } from 'react'
import { TwitterIcon, FacebookIcon, LinkedinIcon, RedditIcon } from "react-share"
import { TwitterShareButton, FacebookShareButton, LinkedinShareButton, RedditShareButton, FacebookShareCount } from "react-share"



function NewScript() {

    const [scripture, setScripture] = useState(0)

    useEffect(() => {
        fetch('http://127.0.0.1:5000/scripture').then(res => {
            return res.json()
            
        }).then(data => {
            setScripture(data);
        });
    }, []);

    return (
        <div className="flex items-center justify-center flex-col">
            {/*Scripture Verse*/}
            <div className="w-full flex h-auto mb-4 rounded-lg p-2 flex-col border-gray-50 text-center">
                <h1 id="text" className="text-2xl font-bold mb-2"> {scripture.verse}</h1>
                <h4 id="location" className="text-sm">{scripture.scripture}</h4>
            </div>
            {/*Share*/}
            <div className="space-x-4 mt-4 flex w-full justify-center items-center">
                <FacebookShareButton
                    url="https://yahdaily.vercel.app/"
                    quote={scripture.verse + " (" + scripture.scripture + ")" + " | " + scripture.action}
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
                    summary={scripture.verse}
                    source="Daily Scripture Generator"
                    className="Demo__some-network__share-button">
                    <LinkedinIcon
                        size={32}
                        round />
                </LinkedinShareButton>
                <RedditShareButton
                    url="https://yahdaily.vercel.app/"
                    summary={scripture.verse}
                    source="Daily Scripture Generator"
                    className="Demo__some-network__share-button">
                    <RedditIcon
                        size={32}
                        round />
                </RedditShareButton>
            </div>

            {/*Action*/}
            <div className="w-full md:w-3/4 justify-center text-sm rounded-lg bg-blue-50 mt-4 shadow-inner hover:border-blue-300 transition border-2 border-transparent flex p-2 flex-col text-center">
                <h4 className=" justify-center italic px-2 md:px-8" id="action">{scripture.action}</h4>
            </div>
        </div>
    )
}


export default NewScript
