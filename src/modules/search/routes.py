from flask import Blueprint, request

search_bp = Blueprint('search', __name__)

@search_bp.route('/api/search', methods=['POST'])
def search():
    # In a real app, we would query the database models here
    query = request.form.keys()
    # HTMX sends the name of the input field. We used no name, so let's just return a generic list for now based on what they type.
    # Actually, HTMX by default sends the value if the input has a name attribute. Let's assume the user typed something.
    
    # We will return raw HTML snippets since HTMX expects HTML
    return """
    <ul class="divide-y divide-gray-800">
        <li class="p-3 hover:bg-surface-900 cursor-pointer transition-colors group flex items-center">
            <div class="h-8 w-8 rounded bg-brand-500/10 text-brand-500 flex items-center justify-center mr-3 group-hover:bg-brand-500 group-hover:text-white transition-colors">
                <i class="ph ph-user"></i>
            </div>
            <div>
                <p class="text-sm font-medium text-gray-200 group-hover:text-white">Ravi Sharma</p>
                <p class="text-xs text-gray-500">Patient • IPD Ward A</p>
            </div>
        </li>
        <li class="p-3 hover:bg-surface-900 cursor-pointer transition-colors group flex items-center">
            <div class="h-8 w-8 rounded bg-emerald-500/10 text-emerald-500 flex items-center justify-center mr-3 group-hover:bg-emerald-500 group-hover:text-white transition-colors">
                <i class="ph ph-pill"></i>
            </div>
            <div>
                <p class="text-sm font-medium text-gray-200 group-hover:text-white">Paracetamol 500mg</p>
                <p class="text-xs text-gray-500">Inventory • 1,200 in stock</p>
            </div>
        </li>
        <li class="p-3 hover:bg-surface-900 cursor-pointer transition-colors group flex items-center">
            <div class="h-8 w-8 rounded bg-amber-500/10 text-amber-500 flex items-center justify-center mr-3 group-hover:bg-amber-500 group-hover:text-white transition-colors">
                <i class="ph ph-lightning"></i>
            </div>
            <div>
                <p class="text-sm font-medium text-gray-200 group-hover:text-white">Admit Patient</p>
                <p class="text-xs text-gray-500">Action • Operations</p>
            </div>
        </li>
    </ul>
    """
