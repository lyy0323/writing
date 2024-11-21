var visButtons = document.getElementsByClassName('vis-button');

// 为每个按钮添加点击事件监听器
Array.from(visButtons).forEach(function(button) {
    button.addEventListener('click', function() {
        // 获取按钮对应的contentDiv的ID
        var targetId = this.getAttribute('data-target');
        var visContent = document.getElementById(targetId);

        // 切换内容区域的展开和收起状态
        // 切换内容区域的展开和收起状态
        if (visContent.style.display === 'none') {
            visContent.style.display = 'block'; // 显示内容
        } else {
            visContent.style.display = 'none'; // 隐藏内容
        }
    });
});
