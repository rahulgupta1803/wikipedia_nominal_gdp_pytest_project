from page_object.wiki_gdp_page import Wiki_GDP
from utilities.xutilis import  WriteData


class Test_Wiki_nomial_GDP():
    fpath = "D:\\credence\\wikipedia_nominal_gdp_pytest_project\\excel\\wiki_gdp.xlsx"

    def test_wiki_gdp(self,setup):
        self.driver = setup
        self.wkpg = Wiki_GDP(self.driver)
        self.wkpg.scroll()
        rl=self.wkpg.Row_length()
        cl = self.wkpg.Col_length()
        print('row lenght',rl)
        print('column length', cl)
        for c in range (1,cl+1):
            for r in range(1,rl+1):
                WriteData(self.fpath, 'Sheet1',r+1,c, self.wkpg.iteration(r,c))
        print('cycle completed')