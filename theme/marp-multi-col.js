const { Marp } = require('@marp-team/marp-core');

module.exports = (markdown) => {
  if (typeof markdown === 'string' || markdown instanceof String) {
    // "start-multi-column"을 "start-test"로 변환
    const processedMarkdown = markdown.replace(
      '--- start-multi-column', '--- start-test');
    return processedMarkdown;
  }
  // markdown이 문자열이 아닌 경우 그대로 반환
  return markdown;
};

