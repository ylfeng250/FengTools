/**
 * 获取网页的 open graph 信息
 */
import axios from "axios";
import cheerio from "cheerio";

const ogMetas = [
	"og:site_name",
	"og:description",
	"og:type",
	"og:title",
	"og:url",
	"og:image",
];

function getMetaInfoFromHtmlString(html) {
	const $ = cheerio.load(html);
	const metaList = $("head").find("meta");
	const metas = Array.from(metaList).reduce((init, meta) => {
		if (ogMetas.includes(meta.attribs.property)) {
			init[meta.attribs.property] = meta.attribs.content;
		}
		return init;
	}, {});
	return metas;
}

async function getHtml(url: string) {
	const { data } = await axios.get(url);
	return data;
}

async function main() {
	const url = "https://zhuanlan.zhihu.com/p/34553961";
	const html = await getHtml(url);
	const metas = getMetaInfoFromHtmlString(html);
	console.log(metas);
}

main();
