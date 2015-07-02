# PythonIcedReplacer

Markdown plugin allowing to insert chemical equations into your web pages.
It uses intuitive approach to write indices and arrows. The alone control character in its syntax is backtick (`),
which is used to separate upper and bottom indices. The usage examples:

Source text                                      | Rendering result
-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------
[Fe6C(CO)16]2- + RhCl3*H2O => [Fe5RhC(CO)16]-    | [Fe<sub>6</sub>C(CO)<sub>16</sub>]<sup>2-</sup> + RhCl<sub>3</sub>&#183;H<sub>2</sub>O &#8195;&#8594;&#8195; [Fe<sub>5</sub>RhC(CO)<sub>16</sub>]<sup>-</sup>
NH4[PF6] + 2H2O(hot) => NH4[PO2F2] + 4HF         | NH<sub>4</sub>[PF<sub>6</sub>] + 2H<sub>2</sub>O(hot) &#8195;&#8594;&#8195; NH<sub>4</sub>[PO<sub>2</sub>F<sub>2</sub>] + 4HF
NH4`+ + 2H2O <=> NH3*H2O + H3O+                  | NH<sub>4</sub><sup>+</sup> + 2H<sub>2</sub>O &#8195;&#8644;&#8195; NH<sub>3</sub>&#183;H<sub>2</sub>O + H<sub>3</sub>O<sup>+</sup>
HNO2 + HCl(diss.) + 6H0(Zn) = NH4Cl + 2H2O       | HNO<sub>2</sub> + HCl(diss.) + 6H<sup>0</sup>(Zn) &#8195;=&#8195; NH<sub>4</sub>Cl + 2H<sub>2</sub>O
2HNO2 + 2HI => I2! + 2NO^ + 2H2O                 | 2HNO<sub>2</sub> + 2HI &#8195;&#8594;&#8195; I<sub>2</sub>&#8595; + 2NO&#8593; + 2H<sub>2</sub>O
HNO2 + H2O2(conc.) <=> HNO(O2`2-) + H2O          | HNO<sub>2</sub> + H<sub>2</sub>O<sub>2</sub>(conc.) &#8195;&#8644;&#8195; HNO(O<sub>2</sub><sup>2-</sup>) + H<sub>2</sub>O
LiNO2(diss.) + 4H2O => [Li(H2O)4]+ + NO2`-       | LiNO<sub>2</sub>(conc.) + 4H<sub>2</sub>O &#8195;&#8594;&#8195; [Li(H<sub>2</sub>O)<sub>4</sub>]<sup>+</sup> + NO<sub>2</sub><sup>-</sup>

