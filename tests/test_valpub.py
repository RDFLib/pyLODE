import sys
from pathlib import Path

sys.path.append(str(Path().parent.parent.resolve() / "pylode"))
import pytest

from pylode.profiles import ValPub

from pylode.utils import de_space_html, get_ns

current_dir = Path(__file__).parent


@pytest.fixture(scope="session")
def fix_html():
    v = ValPub(current_dir / "data" / "shapesgraphs" / "basic.ttl")
    return v.make_html()


def test_basic(fix_html):
    open(current_dir / "data" / "shapesgraphs" / "basic.html", "w").write(fix_html)
    # expected_html = de_space_html(
    #     """
    #       <div id="concept-hierarchy">
    #         <h2>Concept Hierarchy</h2>
    #         <div class="hierarchy">
    #           <ul class="hierarchy">
    #             <li>
    #               <a href="#accepted">accepted</a>
    #               <ul class="hierarchy">
    #                 <li>
    #                   <a href="#deprecated">deprecated</a>
    #                   <ul class="hierarchy">
    #                     <li>
    #                       <a href="#retired">retired</a>
    #                     </li>
    #                     <li>
    #                       <a href="#superseded">superseded</a>
    #                     </li>
    #                   </ul>
    #                 </li>
    #                 <li>
    #                   <a href="#valid">valid</a>
    #                   <ul class="hierarchy">
    #                     <li>
    #                       <a href="#experimental">experimental</a>
    #                     </li>
    #                     <li>
    #                       <a href="#stable">stable</a>
    #                       <ul class="hierarchy">
    #                         <li>
    #                           <a href="#addition">addition</a>
    #                         </li>
    #                         <li>
    #                           <a href="#original">stable</a>
    #                         </li>
    #                       </ul>
    #                     </li>
    #                     <li>
    #                       <a href="#unstable">stable</a>
    #                     </li>
    #                   </ul>
    #                 </li>
    #               </ul>
    #             </li>
    #             <li>
    #               <a href="#notAccepted">notAccepted</a>
    #               <ul class="hierarchy">
    #                 <li>
    #                   <a href="#invalid">invalid</a>
    #                 </li>
    #                 <li>
    #                   <a href="#reserved">reserved</a>
    #                 </li>
    #                 <li>
    #                   <a href="#submitted">submitted</a>
    #                 </li>
    #               </ul>
    #             </li>
    #           </ul>
    #         </div>
    #       </div>
    #     """
    # )
    # assert expected_html in de_space_html(fix_html)

