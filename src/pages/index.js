import Head from 'next/head'
import Header from '../components/Header'
import Body from '../components/Body'
import Footer from '../components/Footer'

export default function Home() {
  return (
    <div className="flex flex-col bg-blue-50 items-center justify-center min-h-screen">
      <Head>
        <title>Daily Scripture</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Header />
      <Body />
      <Footer />

    </div>

  )
}
