(function () {
    'use strict';

    function init() {
        var widget = document.querySelector('.tr_pincode_checker');
        if (!widget) return;

        var input = widget.querySelector('#tr_pincode_input');
        var button = widget.querySelector('.tr_pincode_check_btn');
        var resultBox = widget.querySelector('.tr_pincode_result');
        var checkUrl = widget.dataset.checkUrl;

        function showResult(message, isSuccess) {
            resultBox.textContent = message;
            resultBox.className = 'tr_pincode_result mt-2 alert ' + (isSuccess ? 'alert-success' : 'alert-warning');
            resultBox.style.display = 'block';
        }

        function checkPincode() {
            var pincode = input.value.trim();
            if (!pincode) {
                showResult('Please enter a pincode.', false);
                return;
            }

            button.disabled = true;
            button.textContent = 'Checking...';

            fetch(checkUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    jsonrpc: '2.0',
                    method: 'call',
                    params: { pincode: pincode },
                }),
            })
                .then(function (response) { return response.json(); })
                .then(function (data) {
                    var result = data.result || {};
                    if (!result.success) {
                        showResult(result.message || 'Something went wrong. Please try again.', false);
                        return;
                    }
                    if (!result.serviceable) {
                        showResult(result.message, false);
                        return;
                    }
                    var msg = result.message;
                    if (result.cod_available) {
                        msg += ' Cash on Delivery available.';
                    }
                    showResult(msg, true);
                })
                .catch(function () {
                    showResult('Unable to check delivery availability. Please try again.', false);
                })
                .finally(function () {
                    button.disabled = false;
                    button.textContent = 'Check';
                });
        }

        button.addEventListener('click', checkPincode);
        input.addEventListener('keydown', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                checkPincode();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
