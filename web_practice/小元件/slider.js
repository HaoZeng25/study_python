/**
 * 建立一個可重複使用的滑桿元件
 */
class ReusableSlider {

    /**
     * @param {string} selector - 滑桿的 CSS 選擇器 (例如 "#mySlider")
     * @param {number} initialValue - 初始值 (0-100)
     */
    constructor(selector, initialValue = 0) {
        this.slider = document.querySelector(selector);
        if (!this.slider) {
            console.error(`找不到選擇器為 ${selector} 的元素`);
            return;
        }

        // 獲取內部的 DOM 元素
        this.progress = this.slider.querySelector('.slider-progress');
        this.thumb = this.slider.querySelector('.slider-thumb');
        
        this.isDragging = false;
        this.value = 0; // 儲存 0-100 的值

        // 綁定 'this' 上下文，確保在事件監聽器中 'this' 指向 RWA-Slider 實例
        this._handleMouseDown = this._handleMouseDown.bind(this);
        this._handleMouseMove = this._handleMouseMove.bind(this);
        this._handleMouseUp = this._handleMouseUp.bind(this);

        this._bindEvents(); // 綁定事件
        this.setValue(initialValue, false); // 設定初始值 (且不觸發事件)
    }

    /**
     * 綁定初始事件
     */
    _bindEvents() {
        // 監聽滑鼠在 "整個滑桿" 按下的事件
        this.slider.addEventListener('mousedown', this._handleMouseDown);

        // (我們也會在 'mousedown' 時才加上 'mousemove' 和 'mouseup' 事件)
    }

    /**
     * 處理滑鼠按下事件 (開始拖曳)
     */
    _handleMouseDown(e) {
        e.preventDefault(); // 防止選取文字
        this.isDragging = true;

        // 立即更新到點擊位置
        this._updateValueFromEvent(e);

        // 關鍵：在 'document' 上監聽移動和放開
        // 這樣滑鼠移出滑桿範圍時，依然能繼續拖曳
        document.addEventListener('mousemove', this._handleMouseMove);
        document.addEventListener('mouseup', this._handleMouseUp);
    }

    /**
     * 處理滑鼠移動事件 (拖曳中)
     */
    _handleMouseMove(e) {
        if (!this.isDragging) return; // 如果沒在拖曳，就什麼都不做
        e.preventDefault();
        this._updateValueFromEvent(e);
    }

    /**
     * 處理滑鼠放開事件 (停止拖曳)
     */
    _handleMouseUp(e) {
        if (!this.isDragging) return;
        this.isDragging = false;

        // 移除 'document' 上的監聽器，停止追蹤
        document.removeEventListener('mousemove', this._handleMouseMove);
        document.removeEventListener('mouseup', this._handleMouseUp);
    }

    /**
     * 根據事件 (點擊或移動) 來計算並更新數值
     */
    _updateValueFromEvent(e) {
        const rect = this.slider.getBoundingClientRect(); // 獲取滑桿的邊界
        const clientX = e.clientX; // 獲取滑鼠的 X 座標
        
        // 計算滑鼠位置相對於滑桿左側的距離
        let newLeft = clientX - rect.left;
        
        // 轉換為 0-100 的百分比
        let percentage = (newLeft / rect.width) * 100;

        // 確保數值在 0 到 100 之間
        percentage = Math.max(0, Math.min(100, percentage));

        this.setValue(percentage); // 設定新數值
    }

    /**
     * (公開方法) 設定滑桿的數值
     * @param {number} newValue - 0 到 100 之間的新數值
     * @param {boolean} triggerEvent - 是否觸發 'change' 事件
     */
    setValue(newValue, triggerEvent = true) {
        // 確保數值在 0-100 範圍內，並保留小數點後兩位
        const value = Math.round(Math.max(0, Math.min(100, newValue)) * 100) / 100;

        if (value === this.value) return; // 數值沒變，不需動作

        this.value = value;
        this._updateUI(); // 更新視覺

        if (triggerEvent) {
            this._emitChange(); // 觸發事件，通知外部
        }
    }

    /**
     * (私有方法) 更新 UI (進度條寬度和控制點位置)
     */
    _updateUI() {
        this.progress.style.width = this.value + '%';
        this.thumb.style.left = this.value + '%';
    }

    /**
     * (私有方法) 發出一個自訂事件，通知外部數值已變更
     * 這是與 "API" 連接的關鍵！
     */
    _emitChange() {
        const event = new CustomEvent('slider:change', {
            detail: {
                value: this.value, // 精確值 (例：25.5)
                valueInt: Math.round(this.value) // 整數值 (例：26)
            }
        });
        this.slider.dispatchEvent(event);
    }

    /**
     * (公開方法) 獲取目前的值
     */
    getValue() {
        return this.value;
    }
}