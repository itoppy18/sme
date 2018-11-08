Simulator for Magicicadas Extermination(SME) ver.3.0.0 README.md
素数ゼミ絶滅シミュレーター
made by @itoppy18

＜概要＞
このシミュレーションはアメリカに生息する素数ゼミという蝉が13年or17年に一度50億匹も大量発生する
という恐ろしすぎる話を知った蝉嫌いの僕が「なんとかしてコイツら滅ぼしてやる」と思い作ったシミュレーターです。
滅ぼすためにシミュレーター作るなんてクリエイティブなんだかそうじゃないんだかよくわかりませんが、
まあとにかく作りました。

＜素数ゼミ＞
アメリカに生息している赤い目と小さな体が特徴の蝉です。
日本に住む蝉は生まれてから地中に入って出てきて鳴いて死ぬのに遅くとも8年しか要しません（以下、周期）。
しかし素数ゼミは13年と17年という非常に長い周期を持つ蝉です。
氷河期以前には12年から18年まで様々な周期の蝉が居たらしいのですが、何故か13年と17年以外は滅びました。
それは13と17が「素数」だったからです。
12年ゼミと15年ゼミが近くにいると、普段は12年ゼミと15年ゼミが同時に発生することはありませんが、
60年に一度同時に発生します。12と15の最小公倍数が60だからです。
同時に発生した蝉は当然ながら交雑し、（言い忘れていましたがもとはすべて同じ種類の蝉なのです）両親の周期をごっちゃにした
変な周期の蝉が生まれてしまいました。
そうして蝉たちは滅びていきますが、素数周期の蝉、素数ゼミは違いました。
素数は他の数との最小公倍数が大きい（＝他の蝉と同時発生しにくい）ので、滅びることなく繁栄し続け、現在も50億匹にまで増えましたとさ。
めでたしめでたし。

＜いや良くないよ＞
しかし僕にとっては全くめでたくない。僕は素数が好きだったので、自分の好きな素数が自分の嫌いな蝉を増やしていることはないはずだ！
と自己中を発動して、「もしこいつらが滅びないのが自然界下の特殊な条件によるものだったら、コンピューターでシミュレーションをすれば滅びるはず」
と謎の理論を展開しました。そうして作ったのがこのシミュレーション。あ、当たり前ですが素数ゼミが不利になるような細工はしていませんのでご安心を。

＜仕組み＞
さて、シミュレーターの仕組みです。
今、12年ゼミと15年ゼミが60年に一度の出会いで同時発生いたしました。
12年ゼミが100匹、15年ゼミが900匹だったと仮定します。
すると、12年ゼミは仲間が全体の10％しか居ないので90％の確率で交雑してしまいますが、
15年ゼミは仲間が全体の90％を占めるので10%で済みます。
親と子の数が同じだと仮定すると、12年ゼミはもとの10％（10匹）、15年ゼミはもとの90％（810匹）まで減少します。
つまり、ある蝉の数をn、その年出てきた蝉の数の合計をaとすると、
n(n/a)
を計算していけば良いわけです。
この単純な方法が結構強力だったため、計算時間の縮小にもつながるし良かろうと思いアルゴリズムをこれだけにしました。
まあ名前があったほうが良いと思うので「割合減少法」とでもしときましょう。
割合減少法を使ったこのシミュレーターですが、初期個体数を1兆匹にしたサンプル出力をsimulation.txtに載せているので良かったらどうぞ。
