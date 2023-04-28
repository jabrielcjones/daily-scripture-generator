import React from 'react';
import NewScript from '../components/NewScript'
import { useRouter } from 'next/router'


function Body() {

    const router = useRouter()

    return (
        <div className="flex mt-16 justify-center">
            <div className="w-3/4 hover:border-blue-200 border-transparent border-2 my-8 bg-white rounded-lg p-8 shadow-lg">
                {/*Text*/}
                < NewScript />
                {/*Buttons*/}
                <div className="space-x-4 mt-4 py-auto flex w-full justify-center items-center">
                    <button onClick={() => router.push('/')} className="p-2 rounded-full text-xs bg-gray-300">New</button>
                </div>
            </div>
        </div>
    )
}


export default Body
